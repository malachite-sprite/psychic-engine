# psychic-engine
A first attempt at a 2d game

## The Idea
To create a voice controlled, squad based game. All too often in movies and tv we see
someone sitting back at HQ with a radio and a live feed to their troops on the ground.
What I'd like to do is re-create that, using voice recognition, NLP, and some good ol'
2D animation. It'll be slow going with work (and soon enough, school), but I hope to 
organize this enough to be able to make some progress on weekends. 

## TODO: Total: 26 days (of undestracted work time)
#### Initially: 1 day
- [X] set up project structure

#### Getting the Structure: 5 days
- [ ] (2) get starting with cocos
    - [X] implement a basic app
    - [ ] add a simple moveable character (basically a box)
- [ ] (3) get started with wit
    - [X] add text entry box to app
    - [X] get simple wit connection set up
    - [ ] get character to respond to simple commands

#### Adding some Depth: 13 days
- [ ] (3) add scrolling map
    - [ ] add a basic map tiling system
    - [ ] add "objects" in the map (look at collision mechanics)
    - [ ] get map and "objects" to scroll with a character's position (context: current character)
- [ ] (4) flesh out movement
    - [ ] allow moving to objects on the map
    - [ ] allow hiding beside objects on the map
    - [ ] allow "interacting" with objects (simple color change switches, maybe?)
    - [ ] allow ladders (and ramps?)
- [ ] (3) add multiple characters
    - [ ] add support for multiple characters (+ nametags)
    - [ ] allow characters to be specified by commands
    - [ ] have context for current character, which changes scrolling, too
- [ ] (3) add speech recognition
    - [ ] hook into google API?
    - [ ] make sure this works with the wit stuff
    - [ ] remove the console (or hide it, preferably)

#### Fleshing out the Game: >7 days
- [ ] (2) create simple bots
    - [ ] that just stand still
    - [ ] that can be interacted with
- [ ] (>3) give bots AI
    - [ ] simple "chase"
    - [ ] simple "explore"
    - [ ] figure out something interesting, here (ai can make or break a game)
- [ ] (2) create game flow
    - [ ] add menu
    - [ ] some sort of score/incentives

#### Polish: ? days
- [ ] make skeletons for the characters
- [ ] make skins for the characters
- [ ] create a fancy looking map
- [ ] polish up the menu

