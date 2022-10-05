#
# Copyright (C) 2022  Fabrizio Lo Scudo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from datetime import datetime, timedelta


def link_builder(month, day, n):
    return f'/news/2022/{month}/{day}/russia-ukraine-war-list-of-key-events-day-{n}'


def generate_link_list():
    war_start = datetime(2022, 2, 23, 18, 00)
    dt = datetime.now().date() - war_start.date()
    n_days = dt.days
    l = []
    for days in range(70, n_days):
        d = war_start + timedelta(days=days)
        l.append('https://www.aljazeera.com' + link_builder(d.month, d.day, days))
    with open(r'../links.txt', 'w') as fp:
        for item in l:
            fp.write("%s\n" % item)
        print('Done')
