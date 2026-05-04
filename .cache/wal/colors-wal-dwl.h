/* Taken from https://github.com/djpohly/dwl/issues/466 */
#define COLOR(hex)    { ((hex >> 24) & 0xFF) / 255.0f, \
                        ((hex >> 16) & 0xFF) / 255.0f, \
                        ((hex >> 8) & 0xFF) / 255.0f, \
                        (hex & 0xFF) / 255.0f }

static const float rootcolor[]             = COLOR(0x090b15ff);
static const float bordercolor[]           = COLOR(0x35609Fff);
static const float focuscolor[]            = COLOR(0x2F558Eff);
static const float urgentcolor[]           = COLOR(0x355FA0ff);
