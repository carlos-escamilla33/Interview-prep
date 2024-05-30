#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

using namespace std;

#define NUM_CHARS 256

typedef struct trienode {
    struct trienode *children[NUM_CHARS];

    bool terminal;
} trienode;

trienode *createnode() {
    trienode *newnode = malloc(sizeof *newnode);

    for (int i = 0; i < NUM_CHARS; i++) {
        newnode->children[i] = NULL;
    }

    newnode->terminal = false;

    return newnode;
}

int main() {

}