#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.1),
    on April 02, 2019, at 14:08
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
from psychopy.core import getTime




# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.1'
expName = 'localizer'  # from the Builder filename that created this script
expInfo = {'participant': '001'}
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
    originPath='C:\\Users\\Taylor\\Downloads\\CSN Lab\\projects\\round_robin\\scripts\\scanner_portion\\psychopy_scripts\\localizer\\localizer.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logfile = logging.LogFile(filename+'_data.log', level = logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "wait_for_trig"
wait_for_trigClock = core.Clock()
initial_fix = visual.TextStim(win=win, name='initial_fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trials_2"
trials_2Clock = core.Clock()
name = visual.TextStim(win=win, name='name',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trait = visual.TextStim(win=win, name='trait',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "wait_for_trig"-------
t = 0
wait_for_trigClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
initial_trigger = event.BuilderKeyResponse()
# keep track of which components have finished
wait_for_trigComponents = [initial_fix, initial_trigger]
for thisComponent in wait_for_trigComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wait_for_trig"-------
while continueRoutine:
    # get current time
    t = wait_for_trigClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *initial_fix* updates
    if t >= 0.0 and initial_fix.status == NOT_STARTED:
        # keep track of start time/frame for later
        initial_fix.tStart = t
        initial_fix.frameNStart = frameN  # exact frame index
        initial_fix.setAutoDraw(True)
    
    # *initial_trigger* updates
    if t >= 0.0 and initial_trigger.status == NOT_STARTED:
        # keep track of start time/frame for later
        initial_trigger.tStart = t
        initial_trigger.frameNStart = frameN  # exact frame index
        initial_trigger.status = STARTED
        # keyboard checking is just starting
        initial_trigger.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if initial_trigger.status == STARTED:
        theseKeys = event.getKeys(keyList=['apostrophe'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            initial_trigger.keys = theseKeys[-1]  # just the last key pressed
            initial_trigger.rt = initial_trigger.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in wait_for_trigComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait_for_trig"-------
for thisComponent in wait_for_trigComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if initial_trigger.keys in ['', [], None]:  # No response was made
    initial_trigger.keys=None
thisExp.addData('initial_trigger.keys',initial_trigger.keys)
if initial_trigger.keys != None:  # we had a response
    thisExp.addData('initial_trigger.rt', initial_trigger.rt)
thisExp.nextEntry()
# the Routine "wait_for_trig" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('loc.xlsx'),
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
    
    # ------Prepare to start Routine "trials_2"-------
    t = 0
    trials_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    name.setText(target)
    trait.setText(word)
    fixation.setText(fix_sign)
    trigger = event.BuilderKeyResponse()
    response = event.BuilderKeyResponse()
    # keep track of which components have finished
    trials_2Components = [name, trait, fixation, trigger, response]
    for thisComponent in trials_2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trials_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trials_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *name* updates
        if t >= 0.0 and name.status == NOT_STARTED:
            # keep track of start time/frame for later
            name.tStart = t
            name.frameNStart = frameN  # exact frame index
            name.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if name.status == STARTED and t >= frameRemains:
            name.setAutoDraw(False)
        
        # *trait* updates
        if t >= 0.0 and trait.status == NOT_STARTED:
            # keep track of start time/frame for later
            trait.tStart = t
            trait.frameNStart = frameN  # exact frame index
            trait.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trait.status == STARTED and t >= frameRemains:
            trait.setAutoDraw(False)
        
        # *fixation* updates
        if t >= 0.0 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
            fixation.onset = getTime()
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # *trigger* updates
        if t >= 0.0 and trigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            trigger.tStart = t
            trigger.frameNStart = frameN  # exact frame index
            trigger.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trigger.status == STARTED and t >= frameRemains:
            trigger.status = FINISHED
        if trigger.status == STARTED:
            theseKeys = event.getKeys(keyList=['apostrophe', '5'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trigger.keys = theseKeys[-1]  # just the last key pressed
                trigger.rt = trigger.clock.getTime()
        
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t
            response.frameNStart = frameN  # exact frame index
            response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if response.status == STARTED and t >= frameRemains:
            response.status = FINISHED
        if response.status == STARTED:
            theseKeys = event.getKeys(keyList=['6', '7'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                response.keys = theseKeys[-1]  # just the last key pressed
                response.rt = response.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trials_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trials_2"-------
    for thisComponent in trials_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trigger.keys in ['', [], None]:  # No response was made
        trigger.keys=None
    trials_3.addData('trigger.keys',trigger.keys)
    if trigger.keys != None:  # we had a response
        trials_3.addData('trigger.rt', trigger.rt)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys=None
    trials_3.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        trials_3.addData('response.rt', response.rt)
    trials_3.addData('onset', fixation.onset)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
