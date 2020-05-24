import csv


def device_sort(app, pole):
    funnel_by_month = {}
    funnel_template = {'home_page': 1, 'search_page': 1, 'payment_page': 1, 'payment_confirmation_page': 1}
    with open('click_stream/click_stream3.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            page = list(row.items())[1][1][2:]
            event_date = list(row.items())[2][1][:-3]
            appliance = list(row.items())[3][1]
            gender = list(row.items())[4][1]

            if event_date not in funnel_by_month:
                funnel_by_month[event_date] = funnel_template.copy()

            if appliance == app and gender == pole:

                if page == 'home_page':
                    funnel_by_month[event_date]['home_page'] += 1
                elif page == 'search_page':
                    funnel_by_month[event_date]['search_page'] += 1
                elif page == 'payment_page':
                    funnel_by_month[event_date]['payment_page'] += 1
                else:
                    funnel_by_month[event_date]['payment_confirmation_page'] += 1

        month = sorted(funnel_by_month)

        print('\nСтатистика - ', app, '-', pole)

        for key in month:
            print('\n' + key)
            for page in funnel_by_month[key]:
                print(page, str(round(funnel_by_month[key][page])))


device_sort('Desktop', 'Male')
device_sort('Desktop', 'Female')
device_sort('Mobile', 'Male')
device_sort('Mobile', 'Female')
