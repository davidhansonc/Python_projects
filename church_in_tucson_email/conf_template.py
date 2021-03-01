import datetime
from linked_list import LinkedList

# update weekly
announcements = """See Jay's email for info on the mountain state conference this weekend. Conference information will be posted on the church in Phoenix website <a href="https://zoom.us/j/3872308362?pwd=bENhZnJ3WFpGUFo1NXArUk5lL2dBUT09">here</a>"""

hwmr_week = 1
HWMR = f"Crystallization-Study of Job, Proverbs, Ecclesiastes, vol. 1, week {hwmr_week}"

def get_schedule(seed):
    # create linked list
    num_groups = 6
    group_chain = LinkedList(1)
    for group in range(2, num_groups + 1):
        group_chain.append(group)
    group_chain.tail.next = group_chain.head

    # produce schedule
    node = group_chain.search(group_seed)
    schedule = []
    for day in range(0,6):
        schedule.append(node.value)
        node = node.next
    return schedule

group_seed = 6  # update weekly
schedule = get_schedule(group_seed)

cleaning_team = 4  # update weekly

fri_msg = 15  # update weekly
sat_msg = 55  # update weekly
friday_meeting = f"Life-study of Galatians, msg. {fri_msg}"
saturday_meeting = f"Life-study of Matthew, msg. {sat_msg}"

lords_day = datetime.date.today()
if lords_day.weekday() == 6:
    lords_day += datetime.timedelta(1)
while lords_day.weekday() != 6:
    lords_day += datetime.timedelta(1)

message_html = f"""
<html>
  <head></head>
  <body>
    <h2>Announcements</h2>
        <ul>
            <li>{announcements}
        </ul><br>
    
    <h2>Next Lord's Day ({lords_day})</h2>
        <h3>Prophesying Schedule:</h3>
        <p>
        <i>{HWMR}</i><br>
        <ul>
            <li>No prophesying meeting this week due to conference
            <li>Next week we will repeat week 1 for the prophesying meeting on March 14th also with overflow from this weekend's conference.
        </ul>

        <b>Hall Cleaning (9:00 AM to 9:25 AM):</b><br>
        <ul>
            <li>Team  {cleaning_team}
            <br>** see bottom for group and team info
        </ul>
        </p><br>

    <h2>Meeting Schedule</h2>
        <p>
        Monday:  7:00 PM - Video In the Hall <br><br>

        Tuesday:  7:30 PM - Prayer <br><br>

        Thursday:  7:30 PM - Review of this Week's Holy Word for Morning Revival <br><br>

        Friday:  Cancelled due to conference <br><br>

        Saturday:  Cancelled due to conference <br><br>

        Lord’s Day:  9:30 AM to 10:00 AM Table followed by conference meeting<br><br>

        Zoom in <a href="https://zoom.us/j/3872308362?pwd=bENhZnJ3WFpGUFo1NXArUk5lL2dBUT09">here</a><br>
        Meeting ID: 387 230 8362 <br>
        Password: Kingdom
        </p><br>
    <h3>Cleaning Teams</h3>
        <p>
        Team 1:  Jay, Denny, David, Jessica, Pauline, Phoebe <br>
        Team 2:  Isaac, Esther H., Osvin, Tewei, Millie, Esther <br>
        Team 3:  Craig, Jaime T., Ava, Chien Wei, Josiah, Samuel <br>
        Team 4:  Sam, Joe, Tien Min, Joel, Randy, Carol, Jaime, Teresa
        </p>
  </body>
</html>
"""

message_text = f"""
Announcements:
{announcements}

Next Lord's Day ({lords_day})
Prophesying Schedule:
{HWMR}

No prophesying meeting this week due to conference.
Next week we will repeat week 1 for the prophesying meeting on March 14th also with overflow from this weekend's conference.

    Hall Cleaning (9:00 AM to 9:25 AM):
    Team  {cleaning_team}
    ** see bottom for group and team info

Meeting Schedule
Monday:  7:00 PM - Video In the Hall

Tuesday:  7:30 PM - Prayer

Thursday:  7:30 PM - Review of this Week's Holy Word for Morning Revival

Friday:  Cancelled due to conference

Saturday:  Cancelled due to conference

Lord’s Day:  9:30 AM to 10:00 AM Table followed by conference meeting

Zoom link: https://zoom.us/j/3872308362?pwd=bENhZnJ3WFpGUFo1NXArUk5lL2dBUT09
Meeting ID: 387 230 8362
Password: Kingdom

Cleaning Teams
    Team 1:  Jay, Denny, David, Jessica, Pauline, Phoebe
    Team 2:  Isaac, Esther H., Osvin, Tewei, Millie, Esther
    Team 3:  Craig, Jaime T., Ava, Chien Wei, Josiah, Samuel
    Team 4:  Sam, Joe, Tien Min, Joel, Randy, Carol, Jaime, Teresa
"""