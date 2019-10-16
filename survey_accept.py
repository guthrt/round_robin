#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.1),
    on January 31, 2019, at 10:54
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.1'
expName = 'Survey'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Taylor\\Downloads\\CSN Lab\\Round Robin Project\\Survey.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
start_instructions = visual.TextStim(win=win, name='start_instructions',
    text='For this task, you will rate yourself and your peers on several characteristics.\n\nYour response will remain confidential and will be detached from your name. Please answer as honestly as possible while rating both yourself and your peers. \n\nFor some questions, you may not have a good sense of how that characteristic applies to each of your peers. In these cases, simply make your best guess how much that characteristic applies to that person.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    alignHoriz = 'center',
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text='Press spacebar to continue',
    font='Arial',
    pos=(0, -0.7), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Instructions_2"
Instructions_2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='A question will display at the top of the screen with names and ratings bars below.\n\nUsing the mouse, please click on the scale below each name to rate them on that characteristic. You will rate yourself and your peers on each characteristic.\n\nEach trial is self-paced and you may change your answers while the question is on the screen. Once you are satisfied with your choices, clicking the Accept button under each name will finalize each individual answer. After locking in each rating, you may move on to the next question by pressing the spacebar.',
    font='Arial',
    pos=(0, 0.1), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    alignHoriz = 'center',
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press the Spacebar to continue',
    font='Arial',
    pos=(0, -0.7), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
sample_q = visual.TextStim(win=win, name='sample_q',
    text='default text',
    font='Arial',
    pos=(0, 0.8), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sample_enter = visual.TextStim(win=win, name='sample_enter',
    text='    Click Accept to finalize each \nanswer when you are sure about \n                 each of them ',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=1.5, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sample_next = visual.TextStim(win=win, name='sample_next',
    text='Press Spacebar to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
scale_1 = visual.RatingScale(win=win, name='scale_1', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [-0.5,0.5], scale = None)
scale_1.accept.pos = (-0.5, 0.37)
scale_1.acceptBox.pos = (0.0, 0.1)
scale_2 = visual.RatingScale(win=win, name='scale_2', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [-0.5,0.0], scale = None)
scale_2.accept.pos = (-0.5, -0.13)
scale_2.acceptBox.pos = (0.0, 0.1)
scale_3 = visual.RatingScale(win=win, name='scale_3', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [-0.5,-0.5], scale = None)
scale_3.accept.pos = (-0.5, -0.63)
scale_3.acceptBox.pos = (0.0, 0.1)
scale_4 = visual.RatingScale(win=win, name='scale_4', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [0.5,0.5], scale = None)
scale_4.accept.pos = (0.5, 0.37)
scale_4.acceptBox.pos = (0.0, 0.1)
scale_5 = visual.RatingScale(win=win, name='scale_5', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [0.5,0.0], scale = None)
scale_5.accept.pos = (0.5, -0.13)
scale_5.acceptBox.pos = (0.0, 0.1)
scale_6 = visual.RatingScale(win=win, name='scale_6', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [0.5,-0.5], scale = None)
scale_6.accept.pos = (0.5, -0.63)
scale_6.acceptBox.pos = (0.0, 0.1)
ss1 = visual.TextStim(win=win, name='ss1',
    text='default text',
    font='Arial',
    pos=(-0.8, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
es1 = visual.TextStim(win=win, name='es1',
    text='default text',
    font='Arial',
    pos=(-0.2, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
ss2 = visual.TextStim(win=win, name='ss2',
    text='default text',
    font='Arial',
    pos=(-0.8, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
es2 = visual.TextStim(win=win, name='es2',
    text='default text',
    font='Arial',
    pos=(-0.2, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
ss3 = visual.TextStim(win=win, name='ss3',
    text='default text',
    font='Arial',
    pos=(-0.8, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
es3 = visual.TextStim(win=win, name='es3',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
ss4 = visual.TextStim(win=win, name='ss4',
    text='default text',
    font='Arial',
    pos=(0.2, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
es4 = visual.TextStim(win=win, name='es4',
    text='default text',
    font='Arial',
    pos=(0.8, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
ss5 = visual.TextStim(win=win, name='ss5',
    text='default text',
    font='Arial',
    pos=(0.2, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
es5 = visual.TextStim(win=win, name='es5',
    text='default text',
    font='Arial',
    pos=(0.8, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
ss6 = visual.TextStim(win=win, name='ss6',
    text='default text',
    font='Arial',
    pos=(0.2, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
es6 = visual.TextStim(win=win, name='es6',
    text='default text',
    font='Arial',
    pos=(0.8, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
sample_n1 = visual.TextStim(win=win, name='sample_n1',
    text='default text',
    font='Arial',
    pos=(-0.5, 0.65), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
sample_n2 = visual.TextStim(win=win, name='sample_n2',
    text='default text',
    font='Arial',
    pos=(-0.5, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
sample_n3 = visual.TextStim(win=win, name='sample_n3',
    text='default text',
    font='Arial',
    pos=(-0.5, -0.35), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
sample_n4 = visual.TextStim(win=win, name='sample_n4',
    text='default text',
    font='Arial',
    pos=(0.5, 0.65), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
sample_n5 = visual.TextStim(win=win, name='sample_n5',
    text='default text',
    font='Arial',
    pos=(0.5, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-25.0);
sample_n6 = visual.TextStim(win=win, name='sample_n6',
    text='default text',
    font='Arial',
    pos=(0.5, -0.35), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);

# Initialize components for Routine "Instructions_3"
Instructions_3Clock = core.Clock()
ex_start = visual.TextStim(win=win, name='ex_start',
    text='You will now begin the actual experiment. \n\nPlease let the experimenter know if you have any questions or concerns at this time.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    alignHoriz = 'center',
    depth=0.0);
move_on = visual.TextStim(win=win, name='move_on',
    text='Press the Spacebar to continue',
    font='Arial',
    pos=(0, -0.7), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "all_target_surveys"
all_target_surveysClock = core.Clock()
questions = visual.TextStim(win=win, name='questions',
    text='default text',
    font='Arial',
    pos=(0, 0.8), height=0.08, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    alignHoriz = 'center',
    depth=0.0);
name1_scale = visual.RatingScale(win=win, name='name1_scale', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [-0.5,0.5], scale = None)
name1_scale.accept.pos = (-0.5, 0.37)
name1_scale.acceptBox.pos = (0.0, 0.1)
name2_scale = visual.RatingScale(win=win, name='name2_scale', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [-0.5,0.0], scale = None)
name2_scale.accept.pos = (-0.5, -0.13)
name2_scale.acceptBox.pos = (0.0, 0.1)
name3_scale = visual.RatingScale(win=win, name='name3_scale', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [-0.5,-0.5], scale = None)
name3_scale.accept.pos = (-0.5, -0.63)
name3_scale.acceptBox.pos = (0.0, 0.1)
name4_scale = visual.RatingScale(win=win, name='name4_scale', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [0.5,0.5], scale = None)
name4_scale.accept.pos = (0.5, 0.37)
name4_scale.acceptBox.pos = (0.0, 0.1)
name5_scale = visual.RatingScale(win=win, name='name5_scale', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [0.5,0.0], scale = None)
name5_scale.accept.pos = (0.5, -0.13)
name5_scale.acceptBox.pos = (0.0, 0.1)
name6_scale = visual.RatingScale(win=win, name='name6_scale', low = 1, high = 5, acceptSize = 0.5, acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, pos = [0.5,-0.5], scale = None)
name6_scale.accept.pos = (0.5, -0.63)
name6_scale.acceptBox.pos = (0.0, 0.1)
instructions = visual.TextStim(win=win, name='instructions',
    text='    Click Accept to finalize each \nanswer when you are sure about \n                 each of them ',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
name1 = visual.TextStim(win=win, name='name1',
    text='default text',
    font='Arial',
    pos=(-0.5, 0.65), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
name2 = visual.TextStim(win=win, name='name2',
    text='default text',
    font='Arial',
    pos=(-0.5, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
name3 = visual.TextStim(win=win, name='name3',
    text='default text',
    font='Arial',
    pos=(-0.5, -0.35), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
name4 = visual.TextStim(win=win, name='name4',
    text='default text',
    font='Arial',
    pos=(0.5, 0.65), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
name5 = visual.TextStim(win=win, name='name5',
    text='default text',
    font='Arial',
    pos=(0.5, 0.15), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
name6 = visual.TextStim(win=win, name='name6',
    text='default text',
    font='Arial',
    pos=(0.5, -0.35), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
name1ss = visual.TextStim(win=win, name='name1ss',
    text='default text',
    font='Arial',
    pos=(-0.8, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);
name1es = visual.TextStim(win=win, name='name1es',
    text='default text',
    font='Arial',
    pos=(-0.2, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
name2ss = visual.TextStim(win=win, name='name2ss',
    text='default text',
    font='Arial',
    pos=(-0.8, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
name2es = visual.TextStim(win=win, name='name2es',
    text='default text',
    font='Arial',
    pos=(-0.2, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
name3ss = visual.TextStim(win=win, name='name3ss',
    text='default text',
    font='Arial',
    pos=(-0.8, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-19.0);
name3es = visual.TextStim(win=win, name='name3es',
    text='default text',
    font='Arial',
    pos=(-0.2, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
name4ss = visual.TextStim(win=win, name='name4ss',
    text='default text',
    font='Arial',
    pos=(0.2, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);
name4es = visual.TextStim(win=win, name='name4es',
    text='default text',
    font='Arial',
    pos=(0.8, 0.55), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-22.0);
name5ss = visual.TextStim(win=win, name='name5ss',
    text='default text',
    font='Arial',
    pos=(0.2, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-23.0);
name5es = visual.TextStim(win=win, name='name5es',
    text='default text',
    font='Arial',
    pos=(0.8, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-24.0);
name6ss = visual.TextStim(win=win, name='name6ss',
    text='default text',
    font='Arial',
    pos=(0.2, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-25.0);
name6es = visual.TextStim(win=win, name='name6es',
    text='default text',
    font='Arial',
    pos=(0.8, -0.45), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-26.0);
next_question = visual.TextStim(win=win, name='next_question',
    text='Press Space bar to continue ',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-27.0);

# Initialize components for Routine "Instructions_4"
Instructions_4Clock = core.Clock()
self_next = visual.TextStim(win=win, name='self_next',
    text='You have now completed the first section of the experiment.\n\nFor the remaining questions, a single rating bar will appear on the screen. Using the mouse, please click on the scale to make judgements about yourself.\n\nMake sure to pay attention and read the labels on the scale because they will change for certain questions.\n\nJust like before, once you are sure about your answer, you will finalize your response by clicking the Accept button to submit your answer and press the spacebar to move on to the next question.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    alignHoriz = 'center',
    depth=0.0);
moving_on = visual.TextStim(win=win, name='moving_on',
    text='Press the Spacebar to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "self_surveys"
self_surveysClock = core.Clock()
questions_2 = visual.TextStim(win=win, name='questions_2',
    text='default text',
    font='Arial',
    pos=(0, 0.75), height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    alignHoriz = 'center',
    depth=0.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', acceptPreText = 'Select', acceptText = 'Accept?', showValue = False, size=1.5, pos=[0.0, 0.0], low=1, high=5, labels=[''], scale='', showAccept=True) 
ss = visual.TextStim(win=win, name='ss',
    text='default text',
    font='Arial',
    pos=(-0.45, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
es = visual.TextStim(win=win, name='es',
    text='default text',
    font='Arial',
    pos=(0.45, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
s2 = visual.TextStim(win=win, name='s2',
    text='default text',
    font='Arial',
    pos=(-0.228, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
s3 = visual.TextStim(win=win, name='s3',
    text='default text',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
s4 = visual.TextStim(win=win, name='s4',
    text='default text',
    font='Arial',
    pos=(0.228, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
instructions_2 = visual.TextStim(win=win, name='instructions_2',
    text='Click Accept to finalize your answer',
    font='Arial',
    pos=(0, -0.7), height=0.08, wrapWidth=None, ori=0, 
    color='yellow', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
next_question2 = visual.TextStim(win=win, name='next_question2',
    text='Press Spacebar to continue',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "end"
endClock = core.Clock()
ending = visual.TextStim(win=win, name='ending',
    text='You have completed the experiment. \n\nPlease let the experimenter know that you are finished.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    alignHoriz = 'center',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Press the Spacebar to end the experiment',
    font='Arial',
    pos=(0, -0.8), height=0.08, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [start_instructions, text, key_resp_3]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_instructions* updates
    if t >= 0.0 and start_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        start_instructions.tStart = t
        start_instructions.frameNStart = frameN  # exact frame index
        start_instructions.setAutoDraw(True)
    
    # *text* updates
    if t >= 10 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 10 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_2"-------
t = 0
Instructions_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_2Components = [text_2, text_3, key_resp_8]
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_2"-------
while continueRoutine:
    # get current time
    t = Instructions_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *text_3* updates
    if t >= 10 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 10 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_2"-------
for thisComponent in Instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    sample_q.setText(question)
    scale_1.reset()
    scale_2.reset()
    scale_3.reset()
    scale_4.reset()
    scale_5.reset()
    scale_6.reset()
    ss1.setText(start_scale)
    es1.setText(end_scale)
    ss2.setText(start_scale)
    es2.setText(end_scale)
    ss3.setText(start_scale)
    es3.setText(end_scale)
    ss4.setText(start_scale)
    es4.setText(end_scale)
    ss5.setText(start_scale)
    es5.setText(end_scale)
    ss6.setText(start_scale)
    es6.setText(end_scale)
    sample_n1.setText(tar1)
    sample_n2.setText(tar2)
    sample_n3.setText(tar3)
    sample_n4.setText(tar4)
    sample_n5.setText(tar5)
    sample_n6.setText(tar6)
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    practiceComponents = [sample_q, sample_enter, sample_next, scale_1, scale_2, scale_3, scale_4, scale_5, scale_6, ss1, es1, ss2, es2, ss3, es3, ss4, es4, ss5, es5, ss6, es6, sample_n1, sample_n2, sample_n3, sample_n4, sample_n5, sample_n6, key_resp_5]
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sample_q* updates
        if t >= 0.0 and sample_q.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_q.tStart = t
            sample_q.frameNStart = frameN  # exact frame index
            sample_q.setAutoDraw(True)
        
        # *sample_enter* updates
        if t >= 0.0 and sample_enter.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_enter.tStart = t
            sample_enter.frameNStart = frameN  # exact frame index
            sample_enter.setAutoDraw(True)
        
        # *sample_next* updates
        if t >= 0.0 and sample_next.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_next.tStart = t
            sample_next.frameNStart = frameN  # exact frame index
            sample_next.setAutoDraw(False)
        
        # *scale_1* updates
        if t >= 0.0 and scale_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_1.tStart = t
            scale_1.frameNStart = frameN  # exact frame index
            scale_1.setAutoDraw(True)
        # *scale_2* updates
        if t >= 0.0 and scale_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_2.tStart = t
            scale_2.frameNStart = frameN  # exact frame index
            scale_2.setAutoDraw(True)
        # *scale_3* updates
        if t >= 0.0 and scale_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_3.tStart = t
            scale_3.frameNStart = frameN  # exact frame index
            scale_3.setAutoDraw(True)
        # *scale_4* updates
        if t >= 0.0 and scale_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_4.tStart = t
            scale_4.frameNStart = frameN  # exact frame index
            scale_4.setAutoDraw(True)
        # *scale_5* updates
        if t >= 0.0 and scale_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_5.tStart = t
            scale_5.frameNStart = frameN  # exact frame index
            scale_5.setAutoDraw(True)
        # *scale_6* updates
        if t >= 0.0 and scale_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_6.tStart = t
            scale_6.frameNStart = frameN  # exact frame index
            scale_6.setAutoDraw(True)
        
        # *ss1* updates
        if t >= 0.0 and ss1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss1.tStart = t
            ss1.frameNStart = frameN  # exact frame index
            ss1.setAutoDraw(True)
        
        # *es1* updates
        if t >= 0.0 and es1.status == NOT_STARTED:
            # keep track of start time/frame for later
            es1.tStart = t
            es1.frameNStart = frameN  # exact frame index
            es1.setAutoDraw(True)
        
        # *ss2* updates
        if t >= 0.0 and ss2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss2.tStart = t
            ss2.frameNStart = frameN  # exact frame index
            ss2.setAutoDraw(True)
        
        # *es2* updates
        if t >= 0.0 and es2.status == NOT_STARTED:
            # keep track of start time/frame for later
            es2.tStart = t
            es2.frameNStart = frameN  # exact frame index
            es2.setAutoDraw(True)
        
        # *ss3* updates
        if t >= 0.0 and ss3.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss3.tStart = t
            ss3.frameNStart = frameN  # exact frame index
            ss3.setAutoDraw(True)
        
        # *es3* updates
        if t >= 0.0 and es3.status == NOT_STARTED:
            # keep track of start time/frame for later
            es3.tStart = t
            es3.frameNStart = frameN  # exact frame index
            es3.setAutoDraw(True)
        
        # *ss4* updates
        if t >= 0.0 and ss4.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss4.tStart = t
            ss4.frameNStart = frameN  # exact frame index
            ss4.setAutoDraw(True)
        
        # *es4* updates
        if t >= 0.0 and es4.status == NOT_STARTED:
            # keep track of start time/frame for later
            es4.tStart = t
            es4.frameNStart = frameN  # exact frame index
            es4.setAutoDraw(True)
        
        # *ss5* updates
        if t >= 0.0 and ss5.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss5.tStart = t
            ss5.frameNStart = frameN  # exact frame index
            ss5.setAutoDraw(True)
        
        # *es5* updates
        if t >= 0.0 and es5.status == NOT_STARTED:
            # keep track of start time/frame for later
            es5.tStart = t
            es5.frameNStart = frameN  # exact frame index
            es5.setAutoDraw(True)
        
        # *ss6* updates
        if t >= 0.0 and ss6.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss6.tStart = t
            ss6.frameNStart = frameN  # exact frame index
            ss6.setAutoDraw(True)
        
        # *es6* updates
        if t >= 0.0 and es6.status == NOT_STARTED:
            # keep track of start time/frame for later
            es6.tStart = t
            es6.frameNStart = frameN  # exact frame index
            es6.setAutoDraw(True)
        
        # *sample_n1* updates
        if t >= 0.0 and sample_n1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_n1.tStart = t
            sample_n1.frameNStart = frameN  # exact frame index
            sample_n1.setAutoDraw(True)
        
        # *sample_n2* updates
        if t >= 0.0 and sample_n2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_n2.tStart = t
            sample_n2.frameNStart = frameN  # exact frame index
            sample_n2.setAutoDraw(True)
        
        # *sample_n3* updates
        if t >= 0.0 and sample_n3.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_n3.tStart = t
            sample_n3.frameNStart = frameN  # exact frame index
            sample_n3.setAutoDraw(True)
        
        # *sample_n4* updates
        if t >= 0.0 and sample_n4.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_n4.tStart = t
            sample_n4.frameNStart = frameN  # exact frame index
            sample_n4.setAutoDraw(True)
        
        # *sample_n5* updates
        if t >= 0.0 and sample_n5.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_n5.tStart = t
            sample_n5.frameNStart = frameN  # exact frame index
            sample_n5.setAutoDraw(True)
        
        # *sample_n6* updates
        if t >= 0.0 and sample_n6.status == NOT_STARTED:
            # keep track of start time/frame for later
            sample_n6.tStart = t
            sample_n6.frameNStart = frameN  # exact frame index
            sample_n6.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        
        if scale_1.noResponse + scale_2.noResponse + scale_3.noResponse + scale_4.noResponse + scale_5.noResponse + scale_6.noResponse == 0:
            sample_enter.setAutoDraw(False)
            sample_next.setAutoDraw(True)
            if key_resp_5.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_5.rt = key_resp_5.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('scale_1.response', scale_1.getRating())
    trials_2.addData('scale_1.rt', scale_1.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('scale_2.response', scale_2.getRating())
    trials_2.addData('scale_2.rt', scale_2.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('scale_3.response', scale_3.getRating())
    trials_2.addData('scale_3.rt', scale_3.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('scale_4.response', scale_4.getRating())
    trials_2.addData('scale_4.rt', scale_4.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('scale_5.response', scale_5.getRating())
    trials_2.addData('scale_5.rt', scale_5.getRT())
    # store data for trials_2 (TrialHandler)
    trials_2.addData('scale_6.response', scale_6.getRating())
    trials_2.addData('scale_6.rt', scale_6.getRT())
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    trials_2.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials_2.addData('key_resp_5.rt', key_resp_5.rt)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Instructions_3"-------
t = 0
Instructions_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_3Components = [ex_start, move_on, key_resp_6]
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_3"-------
while continueRoutine:
    # get current time
    t = Instructions_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ex_start* updates
    if t >= 0.0 and ex_start.status == NOT_STARTED:
        # keep track of start time/frame for later
        ex_start.tStart = t
        ex_start.frameNStart = frameN  # exact frame index
        ex_start.setAutoDraw(True)
    
    # *move_on* updates
    if t >= 3 and move_on.status == NOT_STARTED:
        # keep track of start time/frame for later
        move_on.tStart = t
        move_on.frameNStart = frameN  # exact frame index
        move_on.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 3 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_3"-------
for thisComponent in Instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys=None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('all_targets.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "all_target_surveys"-------
    t = 0
    all_target_surveysClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    questions.setText(question)
    name1_scale.reset()
    name2_scale.reset()
    name3_scale.reset()
    name4_scale.reset()
    name5_scale.reset()
    name6_scale.reset()
    key_resp_2 = event.BuilderKeyResponse()
    name1.setText(tar1)
    name2.setText(tar2)
    name3.setText(tar3)
    name4.setText(tar4)
    name5.setText(tar5)
    name6.setText(tar6)
    name1ss.setText(start_scale)
    name1es.setText(end_scale)
    name2ss.setText(start_scale)
    name2es.setText(end_scale)
    name3ss.setText(start_scale)
    name3es.setText(end_scale)
    name4ss.setText(start_scale)
    name4es.setText(end_scale)
    name5ss.setText(start_scale)
    name5es.setText(end_scale)
    name6ss.setText(start_scale)
    name6es.setText(end_scale)
    # keep track of which components have finished
    all_target_surveysComponents = [questions, name1_scale, name2_scale, name3_scale, name4_scale, name5_scale, name6_scale, key_resp_2, instructions, name1, name2, name3, name4, name5, name6, name1ss, name1es, name2ss, name2es, name3ss, name3es, name4ss, name4es, name5ss, name5es, name6ss, name6es, next_question]
    for thisComponent in all_target_surveysComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "all_target_surveys"-------
    while continueRoutine:
        # get current time
        t = all_target_surveysClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *questions* updates
        if t >= 0.0 and questions.status == NOT_STARTED:
            # keep track of start time/frame for later
            questions.tStart = t
            questions.frameNStart = frameN  # exact frame index
            questions.setAutoDraw(True)
        # *name1_scale* updates
        if t >= 0.0 and name1_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            name1_scale.tStart = t
            name1_scale.frameNStart = frameN  # exact frame index
            name1_scale.setAutoDraw(True)
        # *name2_scale* updates
        if t >= 0.0 and name2_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            name2_scale.tStart = t
            name2_scale.frameNStart = frameN  # exact frame index
            name2_scale.setAutoDraw(True)
        # *name3_scale* updates
        if t >= 0.0 and name3_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            name3_scale.tStart = t
            name3_scale.frameNStart = frameN  # exact frame index
            name3_scale.setAutoDraw(True)
        # *name4_scale* updates
        if t >= 0.0 and name4_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            name4_scale.tStart = t
            name4_scale.frameNStart = frameN  # exact frame index
            name4_scale.setAutoDraw(True)
        # *name5_scale* updates
        if t >= 0.0 and name5_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            name5_scale.tStart = t
            name5_scale.frameNStart = frameN  # exact frame index
            name5_scale.setAutoDraw(True)
        # *name6_scale* updates
        if t >= 0.0 and name6_scale.status == NOT_STARTED:
            # keep track of start time/frame for later
            name6_scale.tStart = t
            name6_scale.frameNStart = frameN  # exact frame index
            name6_scale.setAutoDraw(True)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        
        # *instructions* updates
        if t >= 0.0 and instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions.tStart = t
            instructions.frameNStart = frameN  # exact frame index
            instructions.setAutoDraw(True)
        
        # *name1* updates
        if t >= 0.0 and name1.status == NOT_STARTED:
            # keep track of start time/frame for later
            name1.tStart = t
            name1.frameNStart = frameN  # exact frame index
            name1.setAutoDraw(True)
        
        # *name2* updates
        if t >= 0.0 and name2.status == NOT_STARTED:
            # keep track of start time/frame for later
            name2.tStart = t
            name2.frameNStart = frameN  # exact frame index
            name2.setAutoDraw(True)
        
        # *name3* updates
        if t >= 0.0 and name3.status == NOT_STARTED:
            # keep track of start time/frame for later
            name3.tStart = t
            name3.frameNStart = frameN  # exact frame index
            name3.setAutoDraw(True)
        
        # *name4* updates
        if t >= 0.0 and name4.status == NOT_STARTED:
            # keep track of start time/frame for later
            name4.tStart = t
            name4.frameNStart = frameN  # exact frame index
            name4.setAutoDraw(True)
        
        # *name5* updates
        if t >= 0.0 and name5.status == NOT_STARTED:
            # keep track of start time/frame for later
            name5.tStart = t
            name5.frameNStart = frameN  # exact frame index
            name5.setAutoDraw(True)
        
        # *name6* updates
        if t >= 0.0 and name6.status == NOT_STARTED:
            # keep track of start time/frame for later
            name6.tStart = t
            name6.frameNStart = frameN  # exact frame index
            name6.setAutoDraw(True)
        
        # *name1ss* updates
        if t >= 0.0 and name1ss.status == NOT_STARTED:
            # keep track of start time/frame for later
            name1ss.tStart = t
            name1ss.frameNStart = frameN  # exact frame index
            name1ss.setAutoDraw(True)
        
        # *name1es* updates
        if t >= 0.0 and name1es.status == NOT_STARTED:
            # keep track of start time/frame for later
            name1es.tStart = t
            name1es.frameNStart = frameN  # exact frame index
            name1es.setAutoDraw(True)
        
        # *name2ss* updates
        if t >= 0.0 and name2ss.status == NOT_STARTED:
            # keep track of start time/frame for later
            name2ss.tStart = t
            name2ss.frameNStart = frameN  # exact frame index
            name2ss.setAutoDraw(True)
        
        # *name2es* updates
        if t >= 0.0 and name2es.status == NOT_STARTED:
            # keep track of start time/frame for later
            name2es.tStart = t
            name2es.frameNStart = frameN  # exact frame index
            name2es.setAutoDraw(True)
        
        # *name3ss* updates
        if t >= 0.0 and name3ss.status == NOT_STARTED:
            # keep track of start time/frame for later
            name3ss.tStart = t
            name3ss.frameNStart = frameN  # exact frame index
            name3ss.setAutoDraw(True)
        
        # *name3es* updates
        if t >= 0.0 and name3es.status == NOT_STARTED:
            # keep track of start time/frame for later
            name3es.tStart = t
            name3es.frameNStart = frameN  # exact frame index
            name3es.setAutoDraw(True)
        
        # *name4ss* updates
        if t >= 0.0 and name4ss.status == NOT_STARTED:
            # keep track of start time/frame for later
            name4ss.tStart = t
            name4ss.frameNStart = frameN  # exact frame index
            name4ss.setAutoDraw(True)
        
        # *name4es* updates
        if t >= 0.0 and name4es.status == NOT_STARTED:
            # keep track of start time/frame for later
            name4es.tStart = t
            name4es.frameNStart = frameN  # exact frame index
            name4es.setAutoDraw(True)
        
        # *name5ss* updates
        if t >= 0.0 and name5ss.status == NOT_STARTED:
            # keep track of start time/frame for later
            name5ss.tStart = t
            name5ss.frameNStart = frameN  # exact frame index
            name5ss.setAutoDraw(True)
        
        # *name5es* updates
        if t >= 0.0 and name5es.status == NOT_STARTED:
            # keep track of start time/frame for later
            name5es.tStart = t
            name5es.frameNStart = frameN  # exact frame index
            name5es.setAutoDraw(True)
        
        # *name6ss* updates
        if t >= 0.0 and name6ss.status == NOT_STARTED:
            # keep track of start time/frame for later
            name6ss.tStart = t
            name6ss.frameNStart = frameN  # exact frame index
            name6ss.setAutoDraw(True)
        
        # *name6es* updates
        if t >= 0.0 and name6es.status == NOT_STARTED:
            # keep track of start time/frame for later
            name6es.tStart = t
            name6es.frameNStart = frameN  # exact frame index
            name6es.setAutoDraw(True)
        
        # *next_question* updates
        if t >= 0.0 and next_question.status == NOT_STARTED:
            # keep track of start time/frame for later
            next_question.tStart = t
            next_question.frameNStart = frameN  # exact frame index
            next_question.setAutoDraw(False)
        
        if name1_scale.noResponse + name2_scale.noResponse + name3_scale.noResponse + name4_scale.noResponse + name5_scale.noResponse + name6_scale.noResponse == 0:
            instructions.setAutoDraw(False)
            next_question.setAutoDraw(True)
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in all_target_surveysComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "all_target_surveys"-------
    for thisComponent in all_target_surveysComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials (TrialHandler)
    trials.addData('name1_scale.response', name1_scale.getRating())
    trials.addData('name1_scale.rt', name1_scale.getRT())
    # store data for trials (TrialHandler)
    trials.addData('name2_scale.response', name2_scale.getRating())
    trials.addData('name2_scale.rt', name2_scale.getRT())
    # store data for trials (TrialHandler)
    trials.addData('name3_scale.response', name3_scale.getRating())
    trials.addData('name3_scale.rt', name3_scale.getRT())
    # store data for trials (TrialHandler)
    trials.addData('name4_scale.response', name4_scale.getRating())
    trials.addData('name4_scale.rt', name4_scale.getRT())
    # store data for trials (TrialHandler)
    trials.addData('name5_scale.response', name5_scale.getRating())
    trials.addData('name5_scale.rt', name5_scale.getRT())
    # store data for trials (TrialHandler)
    trials.addData('name6_scale.response', name6_scale.getRating())
    trials.addData('name6_scale.rt', name6_scale.getRT())
    # the Routine "all_target_surveys" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "Instructions_4"-------
t = 0
Instructions_4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_4Components = [self_next, moving_on, key_resp_7]
for thisComponent in Instructions_4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_4"-------
while continueRoutine:
    # get current time
    t = Instructions_4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *self_next* updates
    if t >= 0.0 and self_next.status == NOT_STARTED:
        # keep track of start time/frame for later
        self_next.tStart = t
        self_next.frameNStart = frameN  # exact frame index
        self_next.setAutoDraw(True)
    
    # *moving_on* updates
    if t >= 7 and moving_on.status == NOT_STARTED:
        # keep track of start time/frame for later
        moving_on.tStart = t
        moving_on.frameNStart = frameN  # exact frame index
        moving_on.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 7 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_4"-------
for thisComponent in Instructions_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys=None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "Instructions_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('self_surveys.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "self_surveys"-------
    t = 0
    self_surveysClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    questions_2.setText(question)
    rating.reset()
    key_resp_4 = event.BuilderKeyResponse()
    ss.setText(start_scale)
    es.setText(end_scale)
    s2.setText(scale_2)
    s3.setText(scale_3)
    s4.setText(scale_4)
    # keep track of which components have finished
    self_surveysComponents = [questions_2, rating, key_resp_4, ss, es, s2, s3, s4, instructions_2, next_question2]
    for thisComponent in self_surveysComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "self_surveys"-------
    while continueRoutine:
        # get current time
        t = self_surveysClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *questions_2* updates
        if t >= 0.0 and questions_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            questions_2.tStart = t
            questions_2.frameNStart = frameN  # exact frame index
            questions_2.setAutoDraw(True)
        # *rating* updates
        if t >= 0.0 and rating.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating.tStart = t
            rating.frameNStart = frameN  # exact frame index
            rating.setAutoDraw(True)
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        
        # *ss* updates
        if t >= 0.0 and ss.status == NOT_STARTED:
            # keep track of start time/frame for later
            ss.tStart = t
            ss.frameNStart = frameN  # exact frame index
            ss.setAutoDraw(True)
        
        # *es* updates
        if t >= 0.0 and es.status == NOT_STARTED:
            # keep track of start time/frame for later
            es.tStart = t
            es.frameNStart = frameN  # exact frame index
            es.setAutoDraw(True)
        
        # *s2* updates
        if t >= 0.0 and s2.status == NOT_STARTED:
            # keep track of start time/frame for later
            s2.tStart = t
            s2.frameNStart = frameN  # exact frame index
            s2.setAutoDraw(True)
        
        # *s3* updates
        if t >= 0.0 and s3.status == NOT_STARTED:
            # keep track of start time/frame for later
            s3.tStart = t
            s3.frameNStart = frameN  # exact frame index
            s3.setAutoDraw(True)
        
        # *s4* updates
        if t >= 0.0 and s4.status == NOT_STARTED:
            # keep track of start time/frame for later
            s4.tStart = t
            s4.frameNStart = frameN  # exact frame index
            s4.setAutoDraw(True)
        
        # *instructions_2* updates
        if t >= 0.0 and instructions_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructions_2.tStart = t
            instructions_2.frameNStart = frameN  # exact frame index
            instructions_2.setAutoDraw(True)
        
        # *next_question2* updates
        if t >= 0.0 and next_question2.status == NOT_STARTED:
            # keep track of start time/frame for later
            next_question2.tStart = t
            next_question2.frameNStart = frameN  # exact frame index
            next_question2.setAutoDraw(False)
        
        if rating.noResponse == 0:
            instructions_2.setAutoDraw(False)
            next_question2.setAutoDraw(True)
            if key_resp_4.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in self_surveysComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "self_surveys"-------
    for thisComponent in self_surveysComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('rating.response', rating.getRating())
    trials_3.addData('rating.rt', rating.getRT())
    # the Routine "self_surveys" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
endComponents = [ending, key_resp_9, text_4]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ending* updates
    if t >= 0.0 and ending.status == NOT_STARTED:
        # keep track of start time/frame for later
        ending.tStart = t
        ending.frameNStart = frameN  # exact frame index
        ending.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if t >= 5 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
