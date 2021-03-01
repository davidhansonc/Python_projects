import datetime
from linked_list import LinkedList

# update weekly
announcements = """Annual mountain state conference with brother Ron March 5th-7th. More information forthcoming..."""

HWMR = "Crystallization-Study of Job, Proverbs, Ecclesiastes, vol. 1"

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
            <li>Day 1:  Group {schedule[0]}
            <li>Day 2:  Group {schedule[1]}
            <li>Day 3:  Group {schedule[2]}
            <li>Day 4:  Group {schedule[3]}
            <li>Day 5:  Group {schedule[4]}
            <li>Day 6:  Group {schedule[5]}
        </ul>

        <b>Hall Cleaning (9:30 AM to 9:55 AM):</b><br>
        <ul>
            <li>Team  {cleaning_team}
            <br>** see bottom for group and team info
        </ul>
        </p><br>

    <h2>Meeting Schedule</h2>
        <p>
        Lord’s Day:  10:00 AM to Noon(ish) (Lord's table followed by prophesying – please do not be passive in either meeting) <br><br>

        Monday:  7:00 PM - Video In the Hall <br><br>

        Tuesday:  7:30 PM - Prayer <br><br>

        Thursday:  7:30 PM - Review of this Week's Holy Word for Morning Revival <br><br>

        Friday:  7:30 PM  {friday_meeting} <br><br>

        Saturday:  7:30 PM  {saturday_meeting} <br><br>

        Zoom in <a href="https://zoom.us/j/3872308362?pwd=bENhZnJ3WFpGUFo1NXArUk5lL2dBUT09">here</a><br>
        Meeting ID: 387 230 8362 <br>
        Password: Kingdom
        </p><br>
    <h3>Prophesying Groups</h3>
        <p>
        Group 1:  Jay, Randy, Pauline, Kevin <br>
        Group 2:  David, Chien Wei, Denny, Veronica <br>
        Group 3:  Craig, Esther H., Josiah, Tewai, Esther <br>
        Group 4:  Isaac, Millie, Tien Min, Ava, Teresa <br>
        Group 5:  Joel Jaime G., Samuel, Carol <br>
        Group 6:  Sam, Jessica, Phoebe, Joe, Osvin, Jamie T.
        </p>
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
Day 1:  Group {schedule[0]}
Day 2:  Group {schedule[1]}
Day 3:  Group {schedule[2]}
Day 4:  Group {schedule[3]}
Day 5:  Group {schedule[4]}
Day 6:  Group {schedule[5]}

Hall Cleaning (9:30 AM to 9:55 AM):
Team  {cleaning_team}
** see end of email for group and team info


Meeting Schedule
Lord’s Day:  10:00 AM to Noon(ish) (Lord's table followed by prophesying – please do not be passive in either meeting)

Monday:  7:00 PM - Video In the Hall

Tuesday:  7:30 PM - Prayer

Thursday:  7:30 PM - Review of this Week's Holy Word for Morning Revival

Friday:  7:30 PM  {friday_meeting}

Saturday:  7:30 PM  {saturday_meeting}

Zoom link: https://zoom.us/j/3872308362?pwd=bENhZnJ3WFpGUFo1NXArUk5lL2dBUT09
Meeting ID: 387 230 8362
Password: Kingdom


Prophesying Groups:
Group 1:  Jay, Randy, Pauline, Kevin
Group 2:  David, Chien Wei, Denny, Veronica
Group 3:  Craig, Esther H., Josiah, Tewai, Esther
Group 4:  Isaac, Millie, Tien Min, Ava, Teresa
Group 5:  Joel Jaime G., Samuel, Carol
Group 6:  Sam, Jessica, Phoebe, Joe, Osvin, Jamie T.

Cleaning Teams:
Team 1:  Jay, Denny, Kevin, Veronica, Pauline, Phoebe
Team 2:  Isaac, Esther H., Osvin, Tewei, Millie, Esther
Team 3:  Craig, Jaime T., Ava, Chien Wei, Josiah, Samuel
Team 4:  Sam, Joe, Tien Min, Joel, Randy, Carol, Jaime, Teresa
"""