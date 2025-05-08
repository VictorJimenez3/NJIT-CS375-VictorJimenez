import re
import pandas as pd

raw_text = """
2016-17

FIRST TEAM

F: LeBron James, Cleveland Cavaliers

F: Kawhi Leonard, San Antonio Spurs

C: Anthony Davis, New Orleans Pelicans

G: James Harden, Houston Rockets

G: Russell Westbrook, Oklahoma City Thunder

SECOND TEAM

F: Giannis Antetokounmpo, Milwaukee Bucks

F: Kevin Durant, Golden State Warriors

C: Rudy Gobert, Utah Jazz

G: Stephen Curry, Golden State Warriors

G: Isaiah Thomas, Boston Celtics

THIRD TEAM

F: Draymond Green, Golden State Warriors

F: Jimmy Butler, Chicago Bulls

C: DeAndre Jordan, LA Clippers

G: John Wall, Washington Wizards

G: DeMar DeRozan, Toronto Raptors

* (Voting Totals, PDF)

2015-16

FIRST TEAM

F: LeBron James, Cleveland Cavaliers

F: Kawhi Leonard, San Antonio Spurs

C: DeAndre Jordan, LA Clippers

G: Stephen Curry, Golden State Warriors

G: Russell Westbrook, Oklahoma City Thunder

SECOND TEAM

F: Kevin Durant, Oklahoma City Thunder

F: Draymond Green, Golden State Warriors

C: DeMarcus Cousins, Sacramento Kings

G: Chris Paul, LA Clippers

G: Damian Lillard, Portland Trail Blazers

THIRD TEAM

F: Paul George, Indiana Pacers

F: LaMarcus Aldridge, San Antonio Spurs

C: Andre Drummond, Detroit Pistons

G: Klay Thompson, Golden State Warriors

G: Kyle Lowry, Toronto Raptors

* (Voting Totals, PDF)

2014-15

FIRST TEAM

F: LeBron James, Cleveland Cavaliers

F: Anthony Davis, New Orleans Pelicans

C: Marc Gasol, Memphis Grizzlies

G: Stephen Curry, Golden State Warriors

G: James Harden, Houston Rockets

SECOND TEAM

F: LaMarcus Aldridge, Portland Trail Blazers

F: DeMarcus Cousins, Sacramento Kings

C: Pau Gasol, Chicago Bulls

G: Russell Westbrook, Oklahoma City Thunder

G: Chris Paul, LA Clippers

THIRD TEAM

F: Blake Griffin, LA Clippers

F: Tim Duncan, San Antonio Spurs

C: DeAndre Jordan, LA Clippers

G: Klay Thompson, Golden State Warriors

G: Kyrie Irving, Cleveland Cavaliers

2013-14

FIRST TEAM

F: Kevin Durant, Oklahoma City Thunder

F: LeBron James, Miami Heat

C: Joakim Noah, Chicago Bulls

G: James Harden, Houston Rockets

G: Chris Paul, LA Clippers

SECOND TEAM

F: Blake Griffin, LA Clippers

F: Kevin Love, Minnesota Timberwolves

C: Dwight Howard, Houston Rockets

G: Stephen Curry, Golden State Warriors

G: Tony Parker, San Antonio Spurs

THIRD TEAM

F: Paul George, Indiana Pacers

F: LaMarcus Aldridge, Portland Trail Blazers

C: Al Jefferson, Charlotte Bobcats

G: Goran Dragic, Phoenix Suns

G: Damian Lillard, Portland Trail Blazers

2012-13

FIRST TEAM

F: LeBron James, Miami Heat

F: Kevin Durant, Oklahoma City Thunder

C: Tim Duncan, San Antonio Spurs

G: Kobe Bryant, Los Angeles Lakers

G: Chris Paul, LA Clippers

SECOND TEAM

F: Carmelo Anthony, New York Knicks

F: Blake Griffin, LA Clippers

C: Marc Gasol, Memphis Grizzlies

G: Tony Parker, San Antonio Spurs

G: Russell Westbrook, Oklahoma City Thunder

THIRD TEAM

F: David Lee, Golden State Warriors

F: Paul George, Indiana Pacers

C: Dwight Howard, Los Angeles Lakers

G: Dwyane Wade, Miami Heat

G: James Harden, Houston Rockets

2011-12

FIRST TEAM

F: Kevin Durant, Oklahoma City Thunder

F: LeBron James, Miami Heat

C: Dwight Howard, Orlando Magic

G: Kobe Bryant, Los Angeles Lakers

G: Chris Paul, LA Clippers

SECOND TEAM

F: Kevin Love, Minnesota Timberwolves

F: Blake Griffin, LA Clippers

C: Andrew Bynum, Los Angeles Lakers

G: Tony Parker, San Antonio Spurs

G: Russell Westbrook, Oklahoma City Thunder

THIRD TEAM

F: Carmelo Anthony, New York Knicks

F: Dirk Nowitzki, Dallas Mavericks

C: Tyson Chandler, New York Knicks

G: Dwyane Wade, Miami Heat

G: Rajon Rondo, Boston Celtics

2010-11

FIRST TEAM

F: Kevin Durant, Oklahoma City Thunder

F: LeBron James, Miami Heat

C: Dwight Howard, Orlando Magic

G: Kobe Bryant, Los Angeles Lakers

G: Derrick Rose, Chicago Bulls

SECOND TEAM

F: Pau Gasol, Los Angeles Lakers

F: Dirk Nowitzki, Dallas Mavericks

C: Amar’e Stoudemire, New York Knicks

G: Dwyane Wade, Miami Heat

G: Russell Westbrook, Oklahoma City Thunder

THIRD TEAM

F: LaMarcus Aldridge, Portland Trail Blazers

F: Zach Randolph, Memphis Grizzlies

C: Al Horford, Atlanta Hawks

G: Manu Ginobili, San Antonio Spurs

G: Chris Paul, New Orleans Hornets

2009-10

FIRST TEAM

F: Kevin Durant, Oklahoma City Thunder

F: LeBron James, Cleveland Cavaliers

C: Dwight Howard, Orlando Magic

G: Kobe Bryant, Los Angeles Lakers

G: Dwyane Wade, Miami Heat

SECOND TEAM

F: Carmelo Anthony, Denver Nuggets

F: Dirk Nowitzki, Dallas Mavericks

C: Amar’e Stoudemire, Phoenix Suns

G: Steve Nash, Phoenix Suns

G: Deron Williams, Utah Jazz

THIRD TEAM

F: Tim Duncan, San Antonio Spurs

F: Pau Gasol, Los Angeles Lakers

C: Andrew Bogut, Milwaukee Bucks

G: Joe Johnson, Atlanta Hawks

G: Brandon Roy, Portland Trail Blazers

2008-09

FIRST TEAM

F: Dirk Nowitzki, Dallas Mavericks

F: LeBron James, Cleveland Cavaliers

C: Dwight Howard, Orlando Magic

G: Kobe Bryant, Los Angeles Lakers

G: Dwyane Wade, Miami Heat

SECOND TEAM

F: Tim Duncan, San Antonio Spurs

F: Paul Pierce, Boston Celtics

C: Yao Ming, Houston Rockets

G: Chris Paul, New Orleans Hornets

G: Brandon Roy, Portland Trail Blazers

THIRD TEAM

F: Carmelo Anthony, Denver Nuggets

F: Pau Gasol, Los Angeles Lakers

C: Shaquille O’Neal, Phoenix Suns

G: Chauncey Billups, Detroit Pistons

G: Tony Parker, San Antonio Spurs

2007-08

FIRST TEAM

F: Kevin Garnett, Boston Celtics

F: LeBron James, Cleveland Cavaliers

C: Dwight Howard, Orlando Magic

G: Kobe Bryant, Los Angeles Lakers

G: Chris Paul, New Orleans Hornets

SECOND TEAM

F: Tim Duncan, San Antonio Spurs

F: Dirk Nowitzki, Dallas Mavericks

C: Amar’e Stoudemire, Phoenix Suns

G: Steve Nash, Phoenix Suns

G: Deron Williams, Utah Jazz

THIRD TEAM

F: Carlos Boozer, Utah Jazz

F: Paul Pierce, Boston Celtics

C: Yao Ming, Houston Rockets

G: Manu Ginobili, San Antonio Spurs

G: Tracy McGrady, Houston Rockets

2006-07

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Dirk Nowitzki, Dallas Mavericks

C: Amar’e Stoudemire, Phoenix Suns

G: Kobe Bryant, Los Angeles Lakers

G: Steve Nash, Phoenix Suns

SECOND TEAM

F: Chris Bosh, Toronto Raptors

F: LeBron James, Cleveland Cavaliers

C: Yao Ming, Houston Rockets

G: Gilbert Arenas, Washington Wizards

G: Tracy McGrady, Houston Rockets

THIRD TEAM

F: Carmelo Anthony, Denver Nuggets

F: Kevin Garnett, Minnesota Timberwolves

C: Dwight Howard, Orlando Magic

G: Chauncey Billups, Detroit Pistons

G: Dwyane Wade, Miami Heat

2005-06

FIRST TEAM

F: LeBron James, Cleveland Cavaliers

F: Dirk Nowitzki, Dallas Mavericks

C: Shaquille O’Neal, Miami Heat

G: Kobe Bryant, Los Angeles Lakers

G: Steve Nash, Phoenix Suns

SECOND TEAM

F: Elton Brand, LA Clippers

F: Tim Duncan, San Antonio Spurs

C: Ben Wallace, Detroit Pistons

G: Chauncey Billups, Detroit Pistons

G: Dwyane Wade, Miami Heat

THIRD TEAM

F: Carmelo Anthony, Denver Nuggets

F: Shawn Marion, Phoenix Suns

C: Yao Ming, Houston Rockets

G: Gilbert Arenas, Washington Wizards

G: Allen Iverson, Philadelphia 76ers

2004-05

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Dirk Nowitzki, Dallas Mavericks)

C: Shaquille O’Neal, Miami Heat

G: Allen Iverson, Philadelphia 76ers

G: Steve Nash, Phoenix Suns

SECOND TEAM

F: Kevin Garnett, Minnesota Timberwolves

F: LeBron James, Cleveland Cavaliers

C: Amar’e Stoudemire, Phoenix Suns

G: Ray Allen, Seattle SuperSonics

G: Dwyane Wade, Miami Heat

THIRD TEAM

F: Shawn Marion, Phoenix Suns

F: Tracy McGrady, Houston Rockets

C: Ben Wallace, Detroit Pistons

G: Gilbert Arenas, Washington Wizards

G: Kobe Bryant, Los Angeles Lakers

2003-04

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Kevin Garnett, Minnesota Timberwolves

C: Shaquille O’Neal, Los Angeles Lakers

G: Kobe Bryant, Los Angeles Lakers

G: Jason Kidd, New Jersey Nets

SECOND TEAM

F: Tracy McGrady, Orlando Magic

F: Peja Stojakovic, Sacramento Kings

F: Jermaine O’Neal, Indiana Pacers

C: Ben Wallace, Detroit Pistons

G: Sam Cassell, Minnesota Timberwolves

THIRD TEAM

F: Ron Artest, Indiana Pacers

F: Dirk Nowitzki, Dallas Mavericks

C: Yao Ming, Houston Rockets

G: Baron Davis, New Orleans Hornets

G: Michael Redd, Milwaukee Bucks

2002-03

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Kevin Garnett, Minnesota Timberwolves

C: Shaquille O’Neal, Los Angeles Lakers

G: Kobe Bryant, Los Angeles Lakers

G: Tracy McGrady, Orlando Magic

SECOND TEAM

F: Dirk Nowitzki, Dallas Mavericks

F: Chris Webber, Sacramento Kings

C: Ben Wallace, Detroit Pistons

G: Allen Iverson, Philadelphia 76ers

G: Jason Kidd, New Jersey Nets

THIRD TEAM

F: Jamal Mashburn, New Orleans Hornets

F: Paul Pierce, Boston Celtics

C: Jermaine O’Neal, Indiana Pacers

G: Stephon Marbury, Phoenix Suns

G: Steve Nash, Dallas Mavericks

2001-02

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Tracy McGrady, Orlando Magic

C: Shaquille O’Neal, Los Angeles Lakers

G: Kobe Bryant, Los Angeles Lakers

G: Jason Kidd, New Jersey Nets

SECOND TEAM

F: Kevin Garnett, Minnesota Timberwolves

F: Chris Webber, Sacramento Kings

C: Dirk Nowitzki, Dallas Mavericks

G: Allen Iverson, Philadelphia 76ers

G: Gary Payton, Seattle SuperSonics

THIRD TEAM

F: Jermaine O’Neal, Indiana Pacers

F: Ben Wallace, Detroit Pistons

C: Dikembe Mutombo, Philadelphia 76ers

G: Steve Nash, Dallas Mavericks

G: Paul Pierce, Boston Celtics

2000-01

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Chris Webber, Sacramento Kings

C: Shaquille O’Neal, Los Angeles Lakers

G: Allen Iverson, Philadelphia 76ers

G: Jason Kidd, Phoenix Suns

SECOND TEAM

F: Kevin Garnett, Minnesota Timberwolves

F: Vince Carter, Toronto Raptors

C: Dikembe Mutombo, Atlanta Hawks/Philadelphia 76ers

G: Kobe Bryant, Los Angeles Lakers

G: Tracy McGrady, Orlando Magic

THIRD TEAM

F: Karl Malone, Utah Jazz

F: Dirk Nowitzki, Dallas Mavericks

C: David Robinson, San Antonio Spurs

G: Ray Allen, Milwaukee Bucks

G: Gary Payton, Seattle SuperSonic

1999-00

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Kevin Garnett, Minnesota Timberwolves

C: Shaquille O’Neal, Los Angeles Lakers

G: Gary Payton, Seattle SuperSonics

G: Jason Kidd, Phoenix Suns

SECOND TEAM

F: Grant Hill, Detroit Pistons

F: Karl Malone, Utah Jazz

C: Alonzo Mourning, Miami Heat

G: Kobe Bryant, Los Angeles Lakers

G: Allen Iverson, Philadelphia 76ers

THIRD TEAM

F: Vince Carter, Toronto Raptors

F: Chris Webber, Sacramento Kings

C: David Robinson, San Antonio Spurs

G: Eddie Jones, Charlotte Hornets

G: Stephon Marbury, New Jersey Nets

1998-99

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Karl Malone, Utah Jazz

C: Alonzo Mourning, MIami Heat

G: Allen Iverson, Philadelphia 76ers

G: Jason Kidd, Phoenix Suns

SECOND TEAM

F: Grant Hill, Detroit Pistons

F: Chris Webber, Sacramento Kings

C: Shaquille O’Neal, Los Angeles Lakers

G: Tim Hardaway, Miami Heat

G: Gary Payton. Seattle SuperSonics

THIRD TEAM

F: Kevin Garnett, Minnesota Timberwolves

F: Antonio McDyess, Denver Nuggets

C: Hakeem Olajuwon, Houston Rockets

G: Kobe Bryant, Los Angeles Lakers

G: John Stockton, Utah Jazz

1997-98

FIRST TEAM

F: Tim Duncan, San Antonio Spurs

F: Karl Malone, Utah Jazz

C: Shaquille O’Neal, Los Angeles Lakers

G: Michael Jordan, Chicago Bulls

G: Gary Payton, Seattle SuperSonics

SECOND TEAM

F: Grant Hill, Detroit Pistons

F: Vin Baker, Seattle SuperSonics

C: David Robinson, San Antonio Spurs

G: Tim Hardaway, Miami Heat

G: Rod Strickland, Washington Wizards

THIRD TEAM

F: Scottie Pippen, Chicago Bulls

F: Glen Rice, Charlotte Hornets

C: Dikembe Mutombo, Atlanta Hawks

G: Reggie Miller, Indiana Pacers

G: Mitch Richmond, Sacramento Kings

1996-97

FIRST TEAM

F: Grant Hill, Detroit Pistons

F: Karl Malone, Utah Jazz

C: Hakeem Olajuwon, Houston Rockets

G: Michael Jordan, Chicago Bulls

G: Tim Hardaway, Miami Heat

SECOND TEAM

F: Scottie Pippen, Chicago Bulls

F: Glen Rice, Charlotte Hornets

C: Patrick Ewing, New York Knicks

G: Gary Payton, Seattle SuperSonics

G: Mitch Richmond, Sacramento Kings

THIRD TEAM

F: Vin Baker, Milwaukee Bucks

F: Anthony Mason, Charlotte Hornets

C: Shaquille O’Neal, Los Angeles Lakers

G: Anfernee Hardaway, Orlando Magic

G: John Stockton, Utah Jazz

1995-96

FIRST TEAM

F: Scottie Pippen, Chicago Bulls

F: Karl Malone, Utah Jazz

C: David Robinson, San Antonio Spurs

G: Michael Jordan, Chicago Bulls

G: Anfernee Hardaway, Orlando Magic

SECOND TEAM

F: Grant Hill, Detroit PIstons

F: Shawn Kemp, Seattle SuperSonics

C: Hakeem Olajuwon, Houston Rockets

G: Gary Payton, Seattle SuperSonics

G: John Stockton, Utah Jazz

THIRD TEAM

F: Charles Barkley, Phoenix Suns

F: Juwan Howard, Washington Bullets)

C: Shaquille O’Neal, Orlando Magic

G: Reggie Miller, Indiana Pacers

G: Mitch Richmond, Sacramento Kings

1994-95

FIRST TEAM

F: Scottie Pippen, Chicago Bulls

F: Karl Malone, Utah Jazz

C: David Robinson, San Antonio Spurs

G: John Stockton, Utah Jazz

G: Anfernee Hardaway, Orlando Magic

SECOND TEAM

F: Charles Barkley, Phoenix Suns

F: Shawn Kemp, Seattle SuperSonics

C: Shaquille O’Neal, Orlando Magic

G: Gary Payton, Seattle SuperSonics

G: Mitch Richmond, Sacramento Kings

THIRD TEAM

F: Dennis Rodman, San Antonio Spurs

F: Detlef Schrempf, Seattle SuperSonics

C: Hakeem Olajuwon, Houston Rockets

G: Reggie Miller, Indiana Pacers

G: Clyde Drexler, Houston Rockets

1993-94

FIRST TEAM

F: Scottie Pippen, Chicago Bulls

F: Karl Malone, Utah Jazz

C: Hakeem Olajuwon, Houston Rockets

G: John Stockton, Utah Jazz

G: Latrell Sprewell, Golden State Warriors

SECOND TEAM

F: Charles Barkley, Phoenix Suns

F: Shawn Kemp, Seattle SuperSonics

C: David Robinson, San Antonio Spurs

G: Kevin Johnson, Phoenix Suns

G: Mitch Richmond, Sacramento Kings

THIRD TEAM

F: Derrick Coleman, New Jersey Nets

F: Dominique Wilkins, Atlanta Hawks/LA Clippers

C: Shaquille O’Neal, Orlnado Magic

G: Gary Payton, Seattle SuperSonics

G: Mark Price, Cleveland Cavaliers

1992-93

FIRST TEAM

F: Charles Barkley, Phoenix Suns

F: Karl Malone, Utah Jazz

C: Hakeem Olajuwon, Houston Rockets

G: Michael Jordan, Chicago Bulls

G: Mark Price, Cleveland Cavaliers

SECOND TEAM

F: Larry Johnson, Charlotte Hornets

F: Dominique Wilkins, Atlanta Hawks

C: Patrick Ewing, New York Knicks

G: Joe Dumars, Detroit Pistons

G: John Stockton, Utah Jazz

THIRD TEAM

F: Derrick Coleman, New Jersey Nets

F: Scottie Pippen, Chicago Bulls

C: David Robinson, San Antonio Spurs

G: Tim Hardaway, Golden State Warriors

G: Drazen Petrovic, New Jersey Nets

1991-92

FIRST TEAM

F: Chris Mullin, Golden State Warriors

F: Karl Malone, Utah Jazz

C: David Robinson, San Antonio Spurs

G: Michael Jordan, Chicago Bulls

G: Clyde Drexler, Portland Trail Blazers

SECOND TEAM

F: Charles Barkley, Philadelphia 76ers

F: Scottie Pippen, Chicago Bulls

C: Patrick Ewing, New York Knicks

G: Tim Hardaway, Golden State Warriors

G: John Stockton, Utah Jazz

THIRD TEAM

F: Dennis Rodman, Detroit Pistons

F: Kevin Willis, Atlanta Hawks

C: Brad Daugherty, Cleveland Cavaliers

G: Kevin Johnson, Phoenix Suns

G: Mark Price, Cleveland Cavaliers

1990-91

FIRST TEAM

F: Charles Barkley, Philadelphia 76ers

F: Karl Malone, Utah Jazz

C: David Robinson, San Antonio Spurs

G: Michael Jordan, Chicago Bulls

G: Magic Johnson, Los Angeles Lakers

SECOND TEAM

F: Chris Mullin, Golden State Warriors

F: Dominique Wilkins, Atlanta Hawks

C: Patrick Ewing, New York Knicks

G: Clyde Drexler, Portland Trail Blazers

G: Kevin Johnson, Phoenix Suns

THIRD TEAM

F: Bernard King, Washington Bullets

F: James Worthy, Los Angeles Lakers

C: Hakeem Olajuwon, Houston Rockets

G: Joe Dumars, Detroit Pistons

G: John Stockton, Utah Jazz

1989-90

FIRST TEAM

F: Charles Barkley, Philadelphia 76ers

F: Karl Malone, Utah Jazz

C: Patrick Ewing, New York Knicks

G: Michael Jordan, Chicago Bulls

G: Magic Johnson, Los Angeles Lakers

SECOND TEAM

F: Larry Bird, Boston Celtics

F: Tom Chambers, Phoenix Suns

C: Hakeem Olajuwon, Houston Rockets

G: John Stockton, Utah Jazz

G: Kevin Johnson, Phoenix Suns

THIRD TEAM

F: Chris Mullin, Golden State Warriors

F: James Worthy, Los Angeles Lakers

C: David Robinson, San Antonio Spurs

G: Joe Dumars, Detroit Pistons

G: Clyde Drexler, Portland Trail Blazers

1988-89

FIRST TEAM

F: Charles Barkley, Philadelphia 76ers

F: Karl Malone, Utah Jazz

C: Hakeem Olajuwon, Houston Rockets

G: Michael Jordan, Chicago Bulls

G: Magic Johnson, Los Angeles Lakers

SECOND TEAM

F: Chris Mullin, Golden State Warriors

F: Tom Chambers, Phoenix Suns

C: Patrick Ewing, New York Knicks

G: John Stockton, Utah Jazz

G: Kevin Johnson, Phoenix Suns

THIRD TEAM

F: Terry Cummings, Milwaukee Bucks

F: Dominique Wilkins, Atlanta Hawks

C: Robert Parish, Boston Celtics

G: Dale Ellis, Seattle SuperSonics

G: Mark Price, Cleveland Cavaliers


"""
# Continue the block with all years down to 1988-89, then close triple-quote
# For brevity, assume the entire text has been included

# Parsing logic
entries = []
year = None
team = None

for line in raw_text.splitlines():
    line = line.strip()
    # Detect year headers
    m = re.match(r"^(\d{4})-(\d{2})$", line)
    if m:
        start, end = int(m.group(1)), int(m.group(2))
        year = 2000 + end if end < 50 else 1900 + end
        continue
    # Team headings
    if line.upper() == "FIRST TEAM":
        team = "First"
        continue
    if line.upper() == "SECOND TEAM":
        team = "Second"
        continue
    if line.upper() == "THIRD TEAM":
        team = "Third"
        continue
    # Player lines
    m = re.match(r"^(F|G|C):\s*(.+?),", line)
    if m and year and team:
        position = m.group(1)
        player = m.group(2).strip()
        entries.append({
            "Year": year,
            "Player": player,
            "Position": position,
            "Team": team
        })

# Create DataFrame and save
df = pd.DataFrame(entries)
csv_path = "all_nba_correct.csv"
df.to_csv(csv_path, index=False)

