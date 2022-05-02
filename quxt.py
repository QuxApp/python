import math
false = False
true = True

def filter(items, cb):
  filt = []
  for item in items:
    if (cb(item)):
      filt.append(item)
  return filt

def partition(items, cb):
  yes = []
  no = []
  for item in items:
    if (cb(item)):
      yes.append(item)
    else:
      no.append(item)
  return [yes, no]

def matches(rule: dict):
  def fn(obj):
    match = true
    for key in rule:
      if (obj[key] != rule[key]):
        match = false
    return match
      