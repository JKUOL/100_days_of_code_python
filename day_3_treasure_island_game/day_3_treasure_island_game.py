
# press play 

# Start of the game script with a print statement for the game's title and mission
print("Welcome to Treasure Island\nYour mission is to find the treasure")
print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \\ / __| |/ _` | '_ \\ / _` |
| |_| | |  __/ (_| \\__ \\ |_| | | |  __/ \\__ \\ | (_| | | | | (_| |
 \\__|_|  \\___|\\__,_|___/\\__,_|_|  \\___|_|___/_|\\__,_|_| |_|\\__,_|''')

# Ask the player for a direction to start the game
direct = input("\nYou're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

# The main decision branch in the game: the outcome changes based on the input
if direct == "left":
    # Another decision point: choose to wait for a boat or swim across
    action = input("You come to a lake. There is an island in the middle of the lage. Type wait to \"wait\” for a \"boat\". Type swim to swim across\n")
    # ASCII art depicting the scene at the lake
    print('''                                               ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \\O/                                      |\\
          X.a##a.   M                                       |_\\
       .aa########a.>>                                    __|__
    .a################aa.                                 \\   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                 David S. Issel''')
    if action == "wait":
        # Choice of door color, with consequences for each decision
        colour = input("You arrive at the island unharmed There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        # Negative outcome for choosing red or yellow
        if colour == "red" or colour == "yellow":
            print("A bear comes out of the door and mauls you to death: GAME OVER")
            # ASCII art depicting the bear
            print(''' .'"'.        ___,,,___        .'``.
: (\\  `."'"```         ```"'"-'  /) ;
 :  \\                         `./  .'
  `.                            :.'
    /        _         _        \\
   |         0}       {0         |
   |         /         \\         |
   |        /           \\        |
   |       /             \\       |
    \\     |      .-.      |     /
     `.   | . . /   \\ . . |   .'
       `-._\\.'.(     ).'./_.-'
           `\\'  `._.'  '/'
             `. --'-- .'
               `-...-'
''')
        else:
            # Positive outcome for choosing the blue door
            print("Congratulations you won 10 Cro (max. worth of date of recodring 26.05.2023)")
            # ASCII art depicting the winning scenario
            print('''          ____...------------...____
               _.-"` /o/__ ____ __ __  __ \\o\\_`"-._
             .'     / /                    \\ \\     '.
             |=====/o/======================\\o\\=====|
             |____/_/________..____..________\\_\\____|
             /   _/ \\_     <_o#\\__/#o_>     _/ \\_   \\
             \\_________\\####/_________/
              |===\\!/========================\\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \\========|o|===|
              |   | |         \\() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \\__     '-.\\uuu/.-'    __/ \\__ |
              |==== .'.'^'.'.====|
          jgs |  _\\o/   __  {.' __  '.} _   _\\o/  _|
              `""""-""""""""""""""""""""""""""-""""`''')

    else:
        # Negative outcome for choosing to swim
        print("You get eaten by an Alligator: GAME OVER")
        # ASCII art depicting the alligator
        print('''
                                             ___.-----.______
                                   ___.-----'::::::::::::::::`---.___
                _.--._            (:::;,-----'~~~~~`----::::::::::.. `-.
   _          .'_---. `--.__       `~~'                 `~`--.:::::`..  `..
  ; `-.____.-' ' {0} ` `--._`---.____                         `:::::::: : ::
 :_^              ~   `--.___ `----.__`----.____                ~::::::.`;':
  :`--.__,-----.___(         `---.___ `---.___  `----.___         ~|;:,' : |
   `-.___,---.____     _,        ._  `----.____ `----.__ `-----.___;--'  ; :
                  `---' `.  `._    `))  ,  , , `----.____.----.____   --' :|
                        / `,--.\\    `.` `  ` ` ,   ,  ,     _.--   `-----'|'
 _.~~~~~~._____    __./'_/'     :   .:----.___ ` ` ` ``  .-'      , ,  :::'
                 ///--\\;  ____  :   :'    ____`---.___.--::     , ` ` ::'
                 `'           _.'   (    /______     (   `-._   `-._,-'
    ()  ()                 .-' __.-//     /_______---'       `-._   `.
  * *(o)'      ~~~        /////    `'       ~~~~~~      ~~ ______;   ::.
  `\\ )( /*                `'`'                            /_______   _.'
    {()}      ,     ~~~                  ~~~~~~~~           /___.---'  --__
     !|       `                                              ~~~
  ~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')

else:
    # Negative outcome for choosing the right path
    print("The devils spawns and takes your soul: GAME OVER")
    # ASCII art depicting the devil scenario
    print('''   *                       *
            *                 *
           )       (\___/)     (
        * /(       \ (. .)     )\ *
          # )      c\   >'    ( #
           '         )-_/      '
         \\|,    ____| |__    ,|//
           \ )  (  `  ~   )  ( /
            #\ / /| . ' .) \ /#
            | \ / )   , / \ / |
             \,/ ;;,,;,;   \,/
              _,#;,;;,;,
             /,i;;;,,;#,;
            ((  %;;,;,;;,;
             ))  ;#;,;%;;,,
           _//    ;,;; ,#;,
          /_)     #,;  //
                 //    \|_
                 \|_    |#\
                  |#\    -"''')










