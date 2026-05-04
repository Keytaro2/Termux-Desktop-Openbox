const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#090b15", /* black   */
  [1] = "#2F558E", /* red     */
  [2] = "#35609F", /* green   */
  [3] = "#355FA0", /* yellow  */
  [4] = "#3967AC", /* blue    */
  [5] = "#3B6BB3", /* magenta */
  [6] = "#3D6EBA", /* cyan    */
  [7] = "#c1c2c4", /* white   */

  /* 8 bright colors */
  [8]  = "#585b6c",  /* black   */
  [9]  = "#2F558E",  /* red     */
  [10] = "#35609F", /* green   */
  [11] = "#355FA0", /* yellow  */
  [12] = "#3967AC", /* blue    */
  [13] = "#3B6BB3", /* magenta */
  [14] = "#3D6EBA", /* cyan    */
  [15] = "#c1c2c4", /* white   */

  /* special colors */
  [256] = "#090b15", /* background */
  [257] = "#c1c2c4", /* foreground */
  [258] = "#c1c2c4",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
