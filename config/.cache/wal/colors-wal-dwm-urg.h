static const char norm_fg[] = "#c1c2c4";
static const char norm_bg[] = "#090b15";
static const char norm_border[] = "#585b6c";

static const char sel_fg[] = "#c1c2c4";
static const char sel_bg[] = "#35609F";
static const char sel_border[] = "#c1c2c4";

static const char urg_fg[] = "#c1c2c4";
static const char urg_bg[] = "#2F558E";
static const char urg_border[] = "#2F558E";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
