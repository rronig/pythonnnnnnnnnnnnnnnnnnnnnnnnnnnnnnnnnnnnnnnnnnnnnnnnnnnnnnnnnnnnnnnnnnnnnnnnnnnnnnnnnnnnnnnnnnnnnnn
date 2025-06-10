contact_info={
    "Rron": "+383 45 111 111",
    "Alfabet": "+377 38 020 202"
}
print(contact_info)
numri=contact_info["Rron"]
print(numri)
contact_info["Rron"] = "1234567890"
print(contact_info["Rron"])
contact_info["Ard"]="2453423"
print(contact_info)
del contact_info["Ard"]
print(contact_info)
keys=contact_info.keys()
print(keys)
items=contact_info.items()
print(items)