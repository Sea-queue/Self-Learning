/**
 * Vector implementation.
 *
 * - Implement each of the functions to create a working growable array (vector).
 * - Do not change any of the structs
 * - When submitting, You should not have any 'printf' statements in your vector 
 *   functions.
 *
 * IMPORTANT: The initial capacity and the vector's growth factor should be 
 * expressed in terms of the configuration constants in vect.h
 */
#include <assert.h>
#include <stdlib.h>
#include <string.h>

#include "vect.h"

/** Main data structure for the vector. */
struct vect {
  char **data;             /* Array containing the actual data. */
  unsigned int size;       /* Number of items currently in the vector. */
  unsigned int capacity;   /* Maximum number of items the vector can hold before growing. */
};

/** Construct a new empty vector. */
vect_t *vect_new() {

  vect_t* v = (vect_t*)malloc(sizeof(vect_t));
  // *char points to the first char of a string. 
  // we need this because we don't know the lenth of the string,
  // but for queue, we know type long is alway 8 bytes.
  // **char points a first char* in an arry of char* 
  char **data_array = (char**)malloc(VECT_INITIAL_CAPACITY * sizeof(char*));
  v->data = data_array;
  v->size = 0;
  v->capacity = VECT_INITIAL_CAPACITY;
  return v;
}

/** Delete the vector, freeing all memory it occupies. */
void vect_delete(vect_t *v) {
  assert(v != NULL);
  for (int i = 0; i < v->size; i += 1) {
  	free(v->data[i]);
  }
  free(v->data);
  free(v);
}

/** Get the element at the given index. */
const char *vect_get(vect_t *v, unsigned int idx) {
  assert(v != NULL);
  assert(idx < v->size);
  return v->data[idx];
}

/** Get a copy of the element at the given index. The caller is responsible
 *  for freeing the memory occupied by the copy. */
char *vect_get_copy(vect_t *v, unsigned int idx) {
  assert(v != NULL);
  assert(idx < v->size);
  char* element = (char*)malloc((strlen(v->data[idx]) + 1) * sizeof(char));
  strcpy(element, v->data[idx]);
  return element;
}
/** Set the element at the given index. */
void vect_set(vect_t *v, unsigned int idx, const char *elt) {
  assert(v != NULL);
  assert(idx < v->size);
  // in case elt has different length compare with the older value
  free(v->data[idx]);
  v->data[idx] = (char*)malloc((strlen(elt) + 1) * sizeof(char));
  strcpy(v->data[idx], elt);
}

/** Add an element to the back of the vector. */
void vect_add(vect_t *v, const char *elt) {
  assert(v != NULL);
  assert(v->size <= v->capacity);
  
  // make a copy of elt then add.
  // use calloc / realloc
  if (v->size == v->capacity) {
	  unsigned int new_cap = v->capacity * VECT_GROWTH_FACTOR;
	  v->data = realloc(v->data, sizeof(char*)*new_cap);
	  
	  //add the new element
	  v->data[v->size] = (char*)malloc((strlen(elt) + 1) * sizeof(char));
	  strcpy(v->data[v->size], elt); 
	  v->size += 1;
  	  v->capacity = new_cap;
  }
  else {
	  v->data[v->size] = (char*)malloc((strlen(elt) + 1) * sizeof(char));
	  strcpy(v->data[v->size], elt);
	  v->size += 1;
  }
}

/** Remove the last element from the vector. */
void vect_remove_last(vect_t *v) {
  assert(v != NULL);
  free(v->data[v->size - 1]);
  v->size -= 1;
}

/** The number of items currently in the vector. */
unsigned int vect_size(vect_t *v) {
  assert(v != NULL);

  return v->size;
}

/** The maximum number of items the vector can hold before it has to grow. */
unsigned int vect_current_capacity(vect_t *v) {
  assert(v != NULL);

  return v->capacity;
}

