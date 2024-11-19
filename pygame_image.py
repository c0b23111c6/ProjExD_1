import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像Surfaceを作成する
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png") #こうかとんの画像Surfaceを作成する
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    tmr = 0
    xmove_lst = [0, 0, -1, +2, 0]
    ymove_lst = [-1, +1, 0, 0, 0]
    lst_num = 4

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed() 

        if key_lst[pg.K_UP]:
            lst_num = 0
        elif key_lst[pg.K_DOWN]:
            lst_num = 1
        elif key_lst[pg.K_LEFT]:
            lst_num = 2
        elif key_lst[pg.K_RIGHT]:
            lst_num = 3
        kk_rct.move_ip(xmove_lst[lst_num], ymove_lst[lst_num])

        kk_rct.move_ip(-1, 0)


        x = -(tmr%3200) # 練習6-2
        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4800, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()