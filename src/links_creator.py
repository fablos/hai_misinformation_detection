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
