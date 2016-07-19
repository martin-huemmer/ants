#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <string.h>
#include <SDL2/SDL.h>

//gcc -lrt -lSDL2 vis.c

int main() {
	const char *name = "antsfoo";
	const int SIZE = 4096;

	int shm_fd;
	char *ptr;
	int i;

	shm_fd = shm_open(name, O_RDONLY, 0666);
	if (shm_fd == -1) {exit(-1);}

	ptr = mmap(0,SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);
	if (ptr == MAP_FAILED) { exit(-1); }

    //init("lol");
    //atexit(cleanup);


    SDL_Window* window = NULL;
    window = SDL_CreateWindow
    (
        "Jeu de la vie", SDL_WINDOWPOS_UNDEFINED,
        SDL_WINDOWPOS_UNDEFINED,
        999,
        999,
        SDL_WINDOW_SHOWN
    );

    // Setup renderer
    SDL_Renderer* renderer = NULL;
    renderer =  SDL_CreateRenderer( window, -1, SDL_RENDERER_ACCELERATED);

    // Set render color to red ( background will be rendered in this color )
    SDL_SetRenderDrawColor( renderer, 255, 255, 255, 255 );

    // Clear winow
    SDL_RenderClear( renderer );

    // Creat a rect at pos ( 50, 50 ) that's 50 pixels wide and 50 pixels high.
    SDL_Rect r;
    r.x = 0;
    r.y = 0;
    r.w = 4;
    r.h = 4;

    // Set render color to blue ( rect will be rendered in this color )
    SDL_SetRenderDrawColor( renderer, 0, 0, 255, 255 );

    // Render rect
    SDL_RenderFillRect( renderer, &r );

    // Render the rect to the screen
    SDL_RenderPresent(renderer);

    // Wait for 5 sec


    //SDL_DestroyWindow(window);
    //SDL_Quit();


    while (1) {
        SDL_SetRenderDrawColor( renderer, 255, 255, 255, 255 );
        char xs[4];
        strncpy(xs, ptr + 0, 3);
        xs[3] = '\0';
        char ys[4];
        strncpy(ys, ptr + 3, 3);
        ys[3] = '\0';

        printf("%s ", ptr);
        printf("---> %s, %s", xs, ys);

        int x = atoi(xs);
        int y = atoi(ys);

        printf("---> %d, %d\n", x, y);

        r.x=x-2;
        r.y=y-2;
        SDL_RenderClear( renderer );
        SDL_SetRenderDrawColor( renderer, 255, 0, 0, 255 );
        SDL_RenderFillRect( renderer, &r );
        SDL_RenderPresent( renderer);
    }

	return 0;
}