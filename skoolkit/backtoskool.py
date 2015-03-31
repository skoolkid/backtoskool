# -*- coding: utf-8 -*-

# Copyright 2008-2012, 2014, 2015 Richard Dymond (rjdymond@gmail.com)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

try:
    from microsphere import MicrosphereHtmlWriter, MicrosphereAsmWriter, Udg
except ImportError:
    from .microsphere import MicrosphereHtmlWriter, MicrosphereAsmWriter, Udg

class BackToSkoolHtmlWriter(MicrosphereHtmlWriter):
    def init(self):
        MicrosphereHtmlWriter.init(self)
        self.init_lessons(37, 59)
        self.init_characters(183, 209)
        self.font_address = 55040
        self._calculate_tap_index(59392, 88)

    def get_skool_udg(self, y, x, show_chars=False):
        q_addr = x + 46336
        q = self.snapshot[q_addr]
        h = y + 160
        hl = 180 + q // 2 + 256 * h
        i = 0
        if q & 1:
            p = self.snapshot[hl] & 15
        else:
            p = (self.snapshot[hl] & 240) // 16
        if p == 0:
            i = q & 3 or 2
            if q & 1:
                p = self.snapshot[hl + 256] & 15
            else:
                p = (self.snapshot[hl + 256] & 240) // 16
        attr = i | (8 * p)
        ref_addr = q + 256 * h
        ref = self.snapshot[ref_addr]
        a = 136 // 2**(q & 3) & self.snapshot[144 + q // 4 + 256 * h]
        udg_page = (8 if a & 15 else 0) + (144 if a & 240 else 128)
        udg_addr = ref + 256 * udg_page
        udg_bytes = self.snapshot[udg_addr:udg_addr + 2048:256]
        skool_udg = Udg(attr, udg_bytes, q_addr=q_addr, q=q, ref_addr=ref_addr, ref=ref, udg_page=udg_page, x=x, y=y)
        return skool_udg

    def get_sprite_udg(self, state, attr, row, col, udg_page=None):
        as_norm = state | 128
        udg_page = 183 if as_norm < 208 else 199
        col = 2 - col if state & 128 else col
        ref_page = 215 + col * 4 + row
        udg = self._get_sprite_udg(as_norm, attr, ref_page, udg_page)
        if state & 128:
            udg.flip()
        return udg

    def alter_skool_udgs(self, address):
        coords = []
        while True:
            y = self.snapshot[address]
            if y == 255:
                break
            x = self.snapshot[address + 1]
            coords.append((x, y))
            udg_lsb = self.snapshot[address + 2]
            attr = self.snapshot[address + 3]
            d = y + 160
            col_ref = self.snapshot[x + 46336]
            self.snapshot[col_ref + 256 * d] = udg_lsb
            z = 2**(col_ref & 3)
            e = 128 + (col_ref + 104) // 2
            a = self.snapshot[e + 256 * d]
            if col_ref & 1:
                a = (a & 240) | (attr & 15)
            else:
                a = (16 * (attr & 15)) | (a & 15)
            self.snapshot[e + 256 * d] = a
            a = attr & 192
            if a & 64:
                a = a - 56
            e = 144 + col_ref // 4
            self.snapshot[e + 256 * d] = self.snapshot[e + 256 * d] & 255 - 136 // z | a // z
            address += 4
        return coords

    def _get_skool_udgs_by_coords(self, coords):
        left_x, top_y, width, height = self._get_dimensions(coords)
        udg_array = []
        for y in range(top_y, top_y + height):
            udg_array.append([None] * width)
        for x, y in coords:
            udg_array[y - top_y][x - left_x] = self.get_skool_udg(y, x)
        return udg_array

    def _get_dimensions(self, coords, padding=0):
        x_range = [c[0] for c in coords]
        y_range = [c[1] for c in coords]
        left_x = min(x_range)
        top_y = min(y_range)
        width = max(x_range) - left_x + 1
        height = max(y_range) - top_y + 1
        left_x -= padding
        top_y -= padding
        width += 2 * padding if left_x + width < 192 else padding
        height += 2 * padding if top_y + height < 20 else padding
        return left_x, top_y, width, height

    def get_mutable_udg_array(self, address, padding):
        self.push_snapshot()
        coords = self.alter_skool_udgs(address)
        if padding >= 0:
            left_x, top_y, width, height = self._get_dimensions(coords, padding)
            udg_array = self.get_skool_udgs(left_x, top_y, width, height)
        else:
            udg_array = self._get_skool_udgs_by_coords(coords)
        self.pop_snapshot()
        return udg_array

    def get_initial_states(self):
        return [self.snapshot[32 + 256 * c:35 + 256 * c] for c in range(183, 211)]

    def mutable_tiles(self, cwd, name, *addresses):
        objects = []
        prefix = 'c{}_' if name == 'cups' else 'm'
        for address in addresses:
            udgs = self.get_mutable_udg_array(address, -1)
            objects.append(self.write_playarea_tile_table(cwd, udgs, prefix.format(address)))
        return self.format_template(name, {name: objects})

    def _animatory_state_row(self, cwd, state):
        subs = {
            'state_l': state,
            'state_r': state + 128,
            'desc': self.as_descs.get(state, '-'),
            'img_l': self.as_img(cwd, state),
            'img_r': self.as_img(cwd, state + 128)
        }
        return self.format_template('animatory_state_row', subs)

    def keypress_table_rows(self, cwd):
        rows = []
        for index in range(80):
            address = index + 58624
            offset = self.snapshot[address]
            lookup = routine_link = purpose = ''
            if offset:
                lookup = offset + 58624
                routine = self.snapshot[lookup] + 256 * self.snapshot[lookup + 1]
                routine_link = '#R{}'.format(routine)
                purpose = self.keypress_routines[routine]
            subs = {
                'index': index,
                'key': self.get_chr(index + 48),
                'address': address,
                'offset': offset,
                'lookup': lookup,
                'routine': routine_link,
                'purpose': purpose
            }
            rows.append(self.format_template('keypress_table_row', subs))
        return '\n'.join(rows)

    def mutable(self, cwd, address, padding=0):
        fname = 'mutable{0}_{1}'.format(address, padding) if padding else 'mutable{0}'.format(address)
        mutable_path = self.image_path(fname, 'MutableImagePath')
        if self.need_image(mutable_path):
            mutable_udgs = self.get_mutable_udg_array(address, padding)
            self.write_image(mutable_path, mutable_udgs, scale=2)
        return self.img_element(cwd, mutable_path)

    def adjust_mutable(self, cwd, address):
        self.alter_skool_udgs(address)

    def place_char(self, cwd, char_num, x=None, y=None, state=None):
        base_addr = 32 + 256 * char_num
        if state is not None:
            self.snapshot[base_addr] = state
        if x is not None:
            self.snapshot[base_addr + 1] = x
        if y is not None:
            self.snapshot[base_addr + 2] = y

    def hide_chars(self, cwd=None):
        for char_num in range(183, 215):
            self.place_char(cwd, char_num, 200)

class BackToSkoolAsmWriter(MicrosphereAsmWriter):
    pass
