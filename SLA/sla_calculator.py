class SlaCalculator:
    YEAR_SECONDS = 31536000
    MONTH_SECONDS = 2592000
    WEEK_SECONDS = 604800
    DAY_SECONDS = 86400

    class Time:
        @staticmethod
        def human_readable_time(seconds:int):
            precision = '1f'

            if seconds < 60:
                if seconds > 1:
                    return f'%.{precision} Seconds' % seconds
                else:
                    return f'%.{precision} Second' % seconds

            minutes = seconds/60

            if minutes < 60:
                if minutes > 1:
                    return f'%.{precision} Minutes' % minutes
                else:
                    return f'%.{precision} Minute' % minutes

            hours = minutes/60

            if hours < 24:
                if hours > 1:
                    return f'%.{precision} Hours' % hours
                else:
                    return f'%.{precision} Hour' % hours

            days = hours/24

            if days < 365:
                if days < 7:
                    if days > 1:
                        return f'%.{precision} Days' % days
                    else:
                        return f'%.{precision} Day' % days

                weeks = days/7

                if weeks > 1:
                    return f'%.{precision} Weeks' % weeks
                else:
                    return f'%.{precision} Week' % weeks

            else:
                years = days/365

                if years > 1:
                    return f'%.{precision} Years' % years
                else:
                    return f'%.{precision} Year' % years

    class Outage:
        ANNUAL = None
        MONTHLY = None
        WEEKLY = None
        DAILY = None

    @staticmethod
    def get_outage(percentage:float):
        results = SlaCalculator.Outage()
        results.ANNUAL = SlaCalculator.YEAR_SECONDS - (SlaCalculator.YEAR_SECONDS * percentage)/100
        results.MONTHLY = SlaCalculator.MONTH_SECONDS - (SlaCalculator.MONTH_SECONDS * percentage)/100
        results.WEEKLY = SlaCalculator.WEEK_SECONDS - (SlaCalculator.WEEK_SECONDS * percentage)/100
        results.DAILY = SlaCalculator.DAY_SECONDS - (SlaCalculator.DAY_SECONDS * percentage)/100

        return results

    @staticmethod
    def get_sla_report(percentage:float):
        result = SlaCalculator.get_outage(percentage=percentage)

        return f"""
        An uptime of {percentage}, can allow an outage for -

        - {SlaCalculator.Time.human_readable_time(result.ANNUAL)} per Year.
        - {SlaCalculator.Time.human_readable_time(result.MONTHLY)} per Month.
        - {SlaCalculator.Time.human_readable_time(result.WEEKLY)} per Week.
        - {SlaCalculator.Time.human_readable_time(result.DAILY)} per Day.
        """

if __name__ == '__main__':
    print(SlaCalculator.get_sla_report(percentage=99.9))
