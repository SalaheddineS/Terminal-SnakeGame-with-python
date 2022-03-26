import curses
import time
import random
def lol(fen):
    #choisis pair de couleur:
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_RED)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_GREEN)
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    cpt=int(0)
    fen.nodelay(1)
    rapidite=0.05
    key="d"
    snake=[(10,10),(10,11),(10,12),(10,13),(10,14),(10,15),(10,16),(10,17),(10,18),(10,19),(10,20)]
    y=snake[10][0]
    x=snake[10][1]
    food=random.randint(0,curses.LINES-1),random.randint(0,curses.COLS-1)
    while True:
        fen.addstr(0,0,f"SCORE: {cpt}")
        try:
            key=fen.getkey()
        except:
            key=key
        if key == "d":
            x+=1
        elif key=="q":
            x-=1
        elif key=="s":
            y+=1
        elif key=="z":
            y-=1
        if (y,x) in snake :
            fen.clear()
            fen.addstr((curses.LINES-1)//2,(curses.COLS-1)//2,"GAME OVER")
            fen.addstr((curses.LINES-1)//2 +3,(curses.COLS-1)//2 -10,f" VOTRE SCORE EST DE: {cpt} POINTS")
            fen.refresh()
            time.sleep(3)
            break
        snake.append((y,x))
        if snake[len(snake)-1]==food:
            cpt+=1
            food=random.randint(0,curses.LINES-1),random.randint(0,curses.COLS-1)
            rapidite-=0.002
        else:
            snake.pop(0)
        fen.clear()
        for i in snake:
            fen.addstr(0,0,f"SCORE: {cpt}")
            fen.addstr(i[0],i[1]," ",curses.color_pair(2))
        fen.addstr(food[0],food[1]," ",curses.color_pair(1)) 
        fen.refresh()
        time.sleep(rapidite)
   
curses.wrapper(lol)

