from bs4 import BeautifulSoup

# Much of the code below is just the HTML required, line 355 is where the actual processing begins


# Your HTML code (put it in the string below)
# Inspect Element on the homepage >> Find the table, copy paste the code for the table from the webpage
# into the string below, it should be from <tbody> to </tbody> and should contain all <tr></td>'s (table rows)
# with nested <td></td>'s
html = """
<tbody><tr>
        <td colspan="3" align="right"><span id="uiPager"><span id="uiPrevDisabled" style="color: rgb(170, 170, 170);">prev</span><a id="uiPrev" href="#" onclick="prevPage();" style="display: none;">prev</a>&nbsp;<span id="uiPage">[page 1 of 2]</span>&nbsp;<span id="uiNextDisabled" style="display: none; color: #AAA;">next</span><a id="uiNext" href="#" onclick="nextPage();">next</a></span>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>1.</td>
        <td width="480px">Zhang_Syo, Syosset High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:100px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>2.</td>
        <td width="480px">the three nonsensical amigos, The Woodlands School, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:98px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>3.</td>
        <td width="480px">Error 404, Hillsboro-Deering High School, NH</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:97px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>4.</td>
        <td width="480px">EJR, Iroquois Ridge HS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:89px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>5.</td>
        <td width="480px">mecusdonke, Iroquois Ridge HS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:88px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>6.</td>
        <td width="480px">draco and team, White Oaks SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:81px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>7.</td>
        <td width="480px">Jayma, Winston Churchill High School, MD</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:75px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>8.</td>
        <td width="480px">RAM, Donald A. Wilson SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:70px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>9.</td>
        <td width="480px">Taliesin, Richmond Hill HS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:64px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>10.</td>
        <td width="480px">BK Retail, Westford Academy, MA</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:61px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>11.</td>
        <td width="480px">Two musketeers, Westford Academy, MA</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:61px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>12.</td>
        <td width="480px">FunkyMonkeyBoys, Rham High School, CT</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:57px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>13.</td>
        <td width="480px">Goobers, Westford Academy, MA</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:55px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>14.</td>
        <td width="480px">Paragon, White Oaks SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:52px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>15.</td>
        <td width="480px">VPR, North Park SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:48px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>16.</td>
        <td width="480px">devesh co., St. Francis Xavier SS (Dufferin-Peel), ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:35px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>17.</td>
        <td width="480px">YRB, North Park SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:34px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>18.</td>
        <td width="480px">Retailing Rocket, North Park SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:33px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>19.</td>
        <td width="480px">walmart enjoyer, White Oaks SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:31px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>20.</td>
        <td width="480px">Single, Iroquois Ridge HS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:31px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>21.</td>
        <td width="480px">seq, The Woodlands School, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:31px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>22.</td>
        <td width="480px">Hot Shot Pickleball, Plymouth Whitemarsh High School, PA</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:26px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>23.</td>
        <td width="480px">BCAJAG, Great Neck South High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:25px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>24.</td>
        <td width="480px">drippy, Poolesville High School, MD</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:24px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: table-row;">
        <td>25.</td>
        <td width="480px">Dexterous, North Park SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:24px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>26.</td>
        <td width="480px">grishfalzu, Richmond Hill HS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:20px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>27.</td>
        <td width="480px">Muffy&amp;#039;s Pizzeria, Poolesville High School, MD</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:15px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>28.</td>
        <td width="480px">Wheels Up, Holbrook Middle High School, MA</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:15px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>29.</td>
        <td width="480px">S.A. Co, North Park SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:14px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>30.</td>
        <td width="480px">Team Gift, Eastern York High School, PA</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:14px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>31.</td>
        <td width="480px">the wangers, Marc Garneau CI, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:11px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>32.</td>
        <td width="480px">ARMITAGEA, Irondequoit High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:9px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>33.</td>
        <td width="480px">DECA Demons, North Park SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:7px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>34.</td>
        <td width="480px">75 dollars for this_syo, Syosset High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:7px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>35.</td>
        <td width="480px">Real, Iroquois Ridge HS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:7px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>36.</td>
        <td width="480px">Jupiter, Richard Montgomery High School, MD</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:5px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>37.</td>
        <td width="480px">JIANG/THORE, Irondequoit High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:4px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>38.</td>
        <td width="480px">CAREY/GEEZLER, Irondequoit High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:3px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>39.</td>
        <td width="480px">BRAIMANN, Irondequoit High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:1px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>40.</td>
        <td width="480px">Crazy Rich Asians, Academy Of Holy Angels, NJ</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:1px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>41.</td>
        <td width="480px">VINETTEC, Irondequoit High School, NY</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:0px"></div>
        </td>
    </tr>

    <tr class="scoreRow" style="display: none;">
        <td>42.</td>
        <td width="480px">SK, North Park SS, ON</td>
        <td width="100px" align="left">
            <div style="background: #68BBAF; height: 10px; width:0px"></div>
        </td>
    </tr>

</tbody>"""

# Parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Get the element that usually has the name of the team
team_names = soup.find_all("td", {"width": "480px"})

td_div_elements = soup.find_all("td", recursive=True)

# Get all `<div style="background: #68BBAF; height: 10px; width:0px"></div>` from each column, clean it and get px width
pixel_widths = [
    int(td.find("div")["style"].split("width:")[1].split("px")[0])
    for td in td_div_elements
    if td.find("div")
]


print(f"{'Team Name':50}\t{'Percent Score':10}")
for i in range(1, len(team_names)):
    text = team_names[i].get_text(strip=True)
    # Widths range between 0-100 - in other words, it's just percents
    width = pixel_widths[i]
    print(f"{text:50}\t{width:10}")

your_pixel_width = int(input("\nWhat was your pixel width from above? "))
your_score = int(input("\nWhat is your actual score? "))

print(f"{'Team Name':50}\t{'Percent Score':10}\t{'Real Score':10}")
for i in range(1, len(team_names)):
    text = team_names[i].get_text(strip=True)
    width = pixel_widths[i]
    x_factor = (
        your_score / your_pixel_width
    )  # The number that is translating from score to % on the bar
    individual_score = width * x_factor
    print(f"{text:50}\t{width:10}\t{individual_score:10}")
