# The Duckling Race Algorithm

# The problem
# X ducklings are following their mother down a stream
# the ducklings are in order O
# the stream is W units wide
# each duckling is D units in diameter
# and has a max speed of S.
# When their mother calls, which duckling gets to her first?

# Assumptions
# 1. The river is moving at a constant speed.
# 2. It doesn't take the ducklings any extra time to move laterally during a pass.
# 3. The ducklings can each be any size except 0.
# 4. The river is at least as wide as the widest duckling.
# 5. Ducklings are perfectly round (i.e. length = width).
# 6. The mother is stationary.

# Duckling
#   S max speed
#   D diameter
#   P position

# Ideas
# 1. We shouldn't be calculating position at every unit of time, rather, at each event.
# 2. Events: begin, start pass, end pass, duckling reaches mama
# 3. Do we need to recalculate every position for each duckling at each event?

class Duck:
  def __init__(self, name, dia, maxSpeed):
    self.name = name
    self.dia = dia
    self.maxSpeed = maxSpeed
    self.pos = 0
    self.curSpeed = 0
  def __str__(self):
    return "%s is %s units around and has a max speed of %s. %s's position is %s and current speed is %s" % (self.name, self.dia, self.maxSpeed, self.name, self.pos, self.curSpeed)
#  def advance(self):

class Event:
  def __init__(self, ducks, mother=None, time=0, length=0, width=0):
    if mother != None:
      ducks.append(mother)
    self.ducks = ducks
    self.time = time
    self.lenth = length
    self.width = width
    
class Race:
  def __init__(self, ducks, streamWidth):
    self.ducks = ducks
    self.streamWidth = streamWidth
    self.currEvent = None

  def run():
    mother = Duck('mother', 0, 0)
    self.currEvent = Event(self.ducks, mother) # Quaaack! (translation: Go!)
    while mother not in self.currEvent.ducks:
      getNextEvent()
    self.currEvent.ducks.remove(mother)
    return self.currEvent.ducks

  def getNextEvent():
    nextBeginPassEvent = getNextBeginPassEvent()
    nextEndPassEvent = getNextEndPassEvent()
    if nextBeginPassEvent.time < nextEndPassEvent.time:
      currEvent = nextBeginPassEvent
    else: # nextBeginPassEvent.time > nextEndPassEvent.time: # change to else if later
      currEvent = nextEndPassEvent
  #  else: # if nextBeginPassEvent.time == nextEndPassEvent.time:
  #    if nextBeginPassEvent.pos == nextEndPassEvent.pos:
  #      if
  
  def getNextBeginPassEvent(self.currEvent):
    # get list of ducks that are involved in events that happen at next time
    ducksInvolved = getDucksAtNextTime(self.currEvent.ducks)
    
    # remove ducks that aren't in the furthest event group
    ducksInvolved = getLeaders(ducksInvolved)
    
    # remove ducks that won't fit side-by-side
    ducksInvolved = fitDucks(ducksInvolved)
  
    # calculate length and width of event
    length = -1
    width = 0
    for duck in ducksInvolved:
      if length < duck.dia:
        length = duck.dia
    for duck in ducksInvolved:
      width += duck.dia
  
    # caculate the time this event occured
    timeOfThisEvent = self.currEvent.time + shortestCatchupTime
    
    # move ALL the ducks and modify their speed
    ducksInvolved = modifyDucks(ducksInvolved)
  
    # build the event and return it
    return Event(ducksInvolved, None, timeOfThisEvent, lenth, width)
  
  def getNextEndPassEvent():
    return
  
  def catchupTime(firstDuckIndex):
    return abs((ducks[firstDuckIndex].curSpeed - ducks[firstDuckIndex + 1].curSpeed) * (ducks[firstDuckIndex].pos - ducks[firstDuckIndex + 1].pos))
  
  def fitDucks(ducks):
  
    return ducks
  
  # move ducks and modify speed
  # should take the ducks from prevEvent and modify/return as ducks from thisEvent
  def modifyDucks(ducks, catchupTime):
    for duck in ducks:
      duck.pos = duck.pos + (duck.curSpeed * catchupTime)
      duck.curSpeed
    return ducks
  
  def getLeaders(ducks, catchupTime):
    furthestPos = 0
    for duck in ducks:
      nextPos = duck.pos + (duck.curSpeed * catchupTime)
      if furthestPos < nextPos:
        furthestPos = nextPos
    for duck in ducks:
      nextPos = duck.pos + (duck.curSpeed * catchupTime)
      if nextPos != furthestPos:
        ducks.remove(duck)
    return ducks
  
  # get list of ducks that are involved in events that happen at next time
  def getDucksAtNextTime(ducks):
    # first, find the shortest catchup time between any two consec. ducks
    shortestCatchupTime = catchupTime(0, ducks)
    for i in range(len(ducks) - 2):
      if catchupTime(i, ducks) < shortestCatchupTime:
        shortestCatchupTime = catchupTime(i, ducks)
    # second, get the ducks that have these times
    duckInvolved = []
    for i in range(len(ducks) - 2):
      if catchupTime(i, ducks) == shortestCatchupTime:
        ducksInvolved.append(self.currEvent.ducks[i])
    # third, remove duplicate ducks
    return list(set(ducksInvolved))
  

def main():
  ducks = []
  ducks.append(Duck('bill', 3, 4))
  ducks.append(Duck('jill', 2, 5))
  ducks.append(Duck('quill', 4, 3))
  ducks.append(Duck('bob', 7, 1))
  print 'CONTESTENTS:'
  for duck in ducks:
    print duck
  winners = run(ducks)
  print "WINNER(S):"
  for duck in winners:
    print duck

if __name__ == "__main__":main()
