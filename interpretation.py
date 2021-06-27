from Finger import Finger

VERTICAL_ERROR_MARGIN = 10 # FOR FOUR FINGERS: number of pixels allowed to be considered same "level"

def createPositionTuple(lmList):
    '''
    Input: landmark list of 21 landmarks
    Output: Tuple of (IndexPosition, MiddlePosition, RingPosition, PinkyPosition)
    
    Different Positions:
       -> 0: finger is all the way down
       -> 2: finger is all the way up
       -> 1: finger is between up and down (in the middle) 
    '''
    a = analyzeIndexFinger(lmList)
    b = analyzeMiddleFinger(lmList)
    c = analyzeRingFinger(lmList)
    d = analyzePinkyFinger(lmList)
    return (a, b, c, d)


def analyzeIndexFinger(lmList):
    INDEX_FINGER_TIP = lmList[8]
    INDEX_FINGER_DIP = lmList[7]
    INDEX_FINGER_MCP = lmList[5]

    if INDEX_FINGER_TIP[2] > INDEX_FINGER_MCP[2] or abs(
            INDEX_FINGER_TIP[2] - INDEX_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif INDEX_FINGER_TIP[2] < INDEX_FINGER_DIP[2]:
        return 2
    return 1


def analyzeMiddleFinger(lmList):
    MIDDLE_FINGER_TIP = lmList[12]
    MIDDLE_FINGER_DIP = lmList[11]
    MIDDLE_FINGER_MCP = lmList[9]

    if MIDDLE_FINGER_TIP[2] > MIDDLE_FINGER_MCP[2] or abs(
            MIDDLE_FINGER_TIP[2] - MIDDLE_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif MIDDLE_FINGER_TIP[2] < MIDDLE_FINGER_DIP[2]:
        return 2
    return 1


def analyzeRingFinger(lmList):
    RING_FINGER_TIP = lmList[16]
    RING_FINGER_DIP = lmList[15]
    RING_FINGER_MCP = lmList[13]

    if RING_FINGER_TIP[2] > RING_FINGER_MCP[2] or abs(
            RING_FINGER_TIP[2] - RING_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif RING_FINGER_TIP[2] < RING_FINGER_DIP[2]:
        return 2
    return 1


def analyzePinkyFinger(lmList):
    PINKY_FINGER_TIP = lmList[20]
    PINKY_FINGER_DIP = lmList[19]
    PINKY_FINGER_MCP = lmList[17]

    if PINKY_FINGER_TIP[2] > PINKY_FINGER_MCP[2] or abs(
            PINKY_FINGER_TIP[2] - PINKY_FINGER_MCP[2]) < VERTICAL_ERROR_MARGIN:
        return 0
    elif PINKY_FINGER_TIP[2] < PINKY_FINGER_DIP[2]:
        return 2
    return 1

def interpret(lmList) -> 'string':
    fingerPositions = createPositionTuple(lmList)
    if fingerPositions == (2, 2, 2, 2):
        #B
        return "B"
    elif fingerPositions == (2, 2, 2, 0):
        #W
        return "W"
    elif fingerPositions == (2, 2, 0, 0):
        # If depth of middle finger is closer to camera:
        # K
        # If index tip is crossing middle tip:
        # R
        # If index tip is near middle tip:
        # U
        # Else:
        # V
        pass
    elif fingerPositions == (2, 0, 0, 0):
        # If thumb out:
        # L
        # If landmark 8 is lower than 7
        # X
        # Else
        # D
        pass
    elif fingerPositions == (0, 2, 2, 2):
        #F
        return "F"
    elif fingerPositions == (0, 0, 0, 2):
        # If thumb out:
        #     Y
        # Else
        #     I
        pass
    elif fingerPositions == (1, 1, 1, 1):
        #E
        return "E"
    elif fingerPositions == (1, 1, 1, 0):
        #M
        return "M"
    elif fingerPositions == (1, 1, 0, 0):
        #N
        return "N"
    elif fingerPositions == (0, 0, 0, 0):
        # If thumb right of index finger:
        # A
        # If thumb is horizontal:
        # S
        # Else: (Might need to change to t being behind index finger)
        # T
        pass

    else:
        #C and O
        #P and Q
        #G and H
        pass