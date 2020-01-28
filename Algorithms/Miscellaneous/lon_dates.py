import datetime

# def get_lon_dates(go_live_actual, prod_ut_actual):
#     """
#     Each day will be assigned with an index starting from 0-6(monday - sunday), by making use of this index, required
#     day is calulated from go-live event and production uptime event date as reference.
#     :param go_live_actual: date of go_live event
#     :param prod_ut_actual: date of production uptime event
#     :return: dates needs to be considered for comparing post and pre-upgrade metrics
#     """
#     def get_timedelta(date_index):
#         date_index = (7 - (date_index+1)) + 2
#         date_timedelta = datetime.timedelta(date_index)
#         return date_timedelta
#
#     go_live_date = go_live_actual
#     prod_ut_date = prod_ut_actual
#     post_upgrade_date_beginning = datetime.datetime
#     pre_upgrade_date_beginning = prod_ut_date
#     go_live_index = go_live_date.weekday()
#     day_delta = 1
#
#     # If go-live event occurs between sunday to tuesday,
#     # consecutive sunday is considered for metrics comparision.
#     # Otherwise one week is given as a buffer and consecutive sunday is considered.
#     if go_live_actual.weekday() in [6, 0, 1]:
#         if go_live_index == 6:
#             post_upgrade_date_beginning = go_live_actual + datetime.timedelta(7)
#         elif go_live_index == 0:
#             post_upgrade_date_beginning = go_live_actual + datetime.timedelta(6)
#         elif go_live_index == 1:
#             post_upgrade_date_beginning = go_live_actual + datetime.timedelta(5)
#     else:
#         post_upgrade_date_beginning = go_live_actual + get_timedelta(go_live_index)
#
#
#     # With post_upgrade_date_beginning as reference, pre_upgrade_date_beginning is calculated.
#     while post_upgrade_date_beginning.weekday() != pre_upgrade_date_beginning.weekday():
#         pre_upgrade_date_beginning = prod_ut_actual - datetime.timedelta(day_delta)
#         day_delta += 1
#
#     # Converting datetime object to string
#     post_upgrade_date_beginning = datetime.datetime.strftime(
#         post_upgrade_date_beginning, '%m/%d/%Y')
#     pre_upgrade_date_beginning = datetime.datetime.strftime(
#         pre_upgrade_date_beginning, '%m/%d/%Y')
#
#     return {
#         'post_upgrade_beginning': post_upgrade_date_beginning,
#         'pre_upgrade_beginning': pre_upgrade_date_beginning
#     }
#


def get_lon_dates(go_live_actual, prod_ut_actual):

    post_upgrade_date_beginning = go_live_actual
    pre_upgrade_date_beginning = prod_ut_actual

    # By default, first Monday after the go-live is considered for LON data comparision.
    if go_live_actual.weekday() != 0:
        post_upgrade_date_beginning = go_live_actual + \
            datetime.timedelta(6 - go_live_actual.weekday() + 1)

    # Date for pre go-live data comparision is considered w.r.t post_upgrade_date_beginning.
    if prod_ut_actual.weekday() >= go_live_actual.weekday():
        pre_upgrade_date_beginning = prod_ut_actual - datetime.timedelta(prod_ut_actual.weekday() - go_live_actual.weekday()
    elif prod_ut_actual.weekday() < go_live_actual.weekday():
        pre_upgrade_date_beginning=(prod_ut_actual - datetime.timedelta(7)) +
                                    datetime.timedelta(go_live_actual.weekday() -
                                                       prod_ut_actual.weekday())

    # Converting datetime object to string
        post_upgrade_date_beginning=datetime.datetime.strftime(
            post_upgrade_date_beginning, '%m/%d/%Y')
        pre_upgrade_date_beginning=datetime.datetime.strftime(
            pre_upgrade_date_beginning, '%m/%d/%Y')

    return {
            'post_upgrade_beginning': post_upgrade_date_beginning,
            'pre_upgrade_beginning': pre_upgrade_date_beginning
        }

if __name__ == '__main__':
    get_lon_dates()
