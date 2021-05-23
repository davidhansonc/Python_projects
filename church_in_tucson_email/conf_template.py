import datetime
from linked_list import LinkedList

'''UPDATE THE FOLLOWING'''
# update weekly
announcements = """
Hi saints, <br><br>

A few announcements this week. We are resuming the option to Zoom in to the meetings to a degree. There are a few saints that cannot join in person for various reasons, including an elderly couple that will be moving here soon. The option to meet virtually isn't intended for convenience, but if a saint has a particular need, it will be available.
<br><br>

The deadline to register for the semiannual training is next Lord's day May 30th, so don't forget to sign up!
<br><br>

This week we will be in the last week of the current Holy Word for Morning Revival and next week we will get into the recent ITERO. 
<br><br>

This coming weekend is the Memorial day conference. The church here will meet according to the schedule below, but the messages are available over the weekend to all at <a href="conf.lsmwebcast.com">conf.lsmwebcast.com</a>.
<br><br>

Much grace!
"""

hwmr_week = 5  # update weekly (ascending)
group_seed = 6  # update weekly (descending 6-1)
cleaning_team = 4  # update weekly (ascending 1-4)

HWMR = f"""
“The Holy Word for Morning Revival - The Intrinsic and Organic Building Up of the Church as the Body of Christ”, week {hwmr_week}
"""

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

schedule = get_schedule(group_seed)

cleaning_teams = {
        "Team 1":  "Jay, Denny, David, Jessica, Pauline, Phoebe",
        "Team 2":  "Isaac, Esther H., Osvin, Tewei, Millie, Esther",
        "Team 3":  "Craig, Jaime T., Ava, Chien Wei, Josiah, Samuel",
        "Team 4":  "Sam, Joe, Tien Min, Joel, Randy, Carol, Jaime, Teresa"
    }

lords_day = datetime.date.today()
if lords_day.weekday() == 6:
    lords_day += datetime.timedelta(1)
while lords_day.weekday() != 6:
    lords_day += datetime.timedelta(1)

message_html = f"""
<html>
  <head></head>
  <body>
    <p> {announcements} </p><br>

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
            <br>** see bottom for groups
        </ul>

        <b>Hall Cleaning (9:15 AM to 9:45 AM):</b><br>
        <ul>
            <li>Team {cleaning_team} - {cleaning_teams[f"Team {cleaning_team}"]}
        </ul>
        </p><br>

    <h2>This Week's Meeting Schedule</h2>
        <p>
        Monday:  7:00 PM - Video In the Hall <br><br>

        Tuesday:  7:30 PM - Prayer <br><br>

        Thursday:  7:30 PM - Review of this Week's Holy Word for Morning Revival <br><br>

        Friday:  7:00 PM - Memorial Day Conference, message 1 <br><br>

        Saturday morning:  10:00 AM - Memorial Day Conference, message 2 (watch at home) <br><br>

        Saturday evening:  7:00 PM - Memorial Day Conference, message 3 <br><br>

        Lord’s Day morning:  10:00 AM to Noon - The Lord's table followed by prophesying <br><br>

        Lord’s Day evening:  7:00 PM - Memorial Day Conference, message 4 <br><br>

        Monday evening, May 31st: 7:00 PM - Memorial Day Conference, message 5 <br><br>
        
        Monday evening, June 7th: 7:00 PM - Memorial Day Conference, message 6 <br><br>

        The website for streaming the conference messages is <a href="conf.lsmwebcast.com">conf.lsmwebcast.com</a><br><br>

        Zoom in to the church meetings <a href="https://zoom.us/j/3872308362?pwd=bENhZnJ3WFpGUFo1NXArUk5lL2dBUT09">here</a><br>
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
  </body>
</html>
"""

message_text = f"""
If you see this, please reply and ask for a direct email with the schedule and announcements.
"""