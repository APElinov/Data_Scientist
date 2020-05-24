import csv

funnel_by_month = {}
funnel_template = {'home_page': 0, 'search_page': 0, 'payment_page': 0, 'payment_confirmation_page': 0}

with open('click_stream/click_stream.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        page = list(row.items())[1][1][2:]
        event_date = list(row.items())[2][1][:-3]

        if event_date not in funnel_by_month:
            funnel_by_month[event_date] = funnel_template.copy()

        if page == 'home_page':
            funnel_by_month[event_date]['home_page'] += 1
        elif page == 'search_page':
            funnel_by_month[event_date]['search_page'] += 1
        elif page == 'payment_page':
            funnel_by_month[event_date]['payment_page'] += 1
        else:
            funnel_by_month[event_date]['payment_confirmation_page'] += 1

month = sorted(funnel_by_month)

for key in month:
    print('\n' + key)
    for page in funnel_by_month[key]:
        print(page, str(round(funnel_by_month[key][page] /
                              funnel_by_month[key]['home_page'] * 100, 2)) + '%')
