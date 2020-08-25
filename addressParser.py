def stateParser(string):
    string = string.strip()
    states = [
        ["Alabama","AL"],
        ["Alaska","AK"],
        ["Arizona","AZ"],
        ["Arkansas","AR"],
        ["California","CA"],
        ["Colorado","CO"],
        ["Connecticut","CT"],
        ["District of Columbia","DC"],
        ["Delaware","DE"],
        ["Florida","FL"],
        ["Georgia", "GA"],
        ["Hawaii","HI"],
        ["Idaho","ID"],
        ["Illinois","IL"],
        ["Indiana","IN"],
        ["Iowa","IA"],
        ["Kansas","KS"],
        ["Kentucky","KY"],
        ["Louisiana","LA"],
        ["Maine","ME"],
        ["Maryland","MD"],
        ["Massachusetts","MA"],
        ["Michigan","MI"],
        ["Minnesota","MN"],
        ["Mississippi","MS"],
        ["Missouri","MO"],
        ["Montana","MT"],
        ["Nebraska","NE"],
        ["Nevada","NV"],
        ["New Hampshire","NH"],
        ["New Jersey","NJ"],
        ["New Mexico","NM"],
        ["New York","NY"],
        ["North Carolina","NC"],
        ["North Dakota","ND"],
        ["Ohio","OH"],
        ["Oklahoma","OK"],
        ["Oregon","OR"],
        ["Pennsylvania","PA"],
        ["Rhode Island","RI"],
        ["South Carolina","SC"],
        ["South Dakota","SD"],
        ["Tennessee","TN"],
        ["Texas","TX"],
        ["Utah","UT"],
        ["Vermont","VT"],
        ["Virginia","VA"],
        ["Washington","WA"],
        ["West Virginia","WV"],
        ["Wisconsin","WI"],
        ["Wyoming","WY"],
    ]

    result = None

    for state in states:
        hasInitial = string.rfind(state[1])
        if hasInitial != -1:
            # print(f"Address:{string}, Found: {state[1]}")
            result = {"state": state[1], "address": string}
            break
        
        noInitial = string.rfind(state[0])        
        if noInitial != -1:
            # print(f"Address:{string}, Found: {state[1]}")
            string = string.replace(state[0], state[1])
            result = {"state": state[1], "address": string}
            break

    return result