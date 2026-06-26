#!/data/data/com.termux/files/usr/bin/bash
export PATH="/data/data/com.termux/files/usr/bin:$PATH"

# Routes
CACHE_DIR="$HOME/.cache/eww/covers"
DEFAULT_IMG="$HOME/.config/eww/assets/digital-art-cat-pattern.jpg"

mkdir -p "$CACHE_DIR"

# 1. We asked audtool directly.
raw_path=$(audtool current-song-filename 2>/dev/null)

if [[ -z "$raw_path" ]]; then
    echo "$DEFAULT_IMG"
    exit 0
fi

# 2. If there is a path, we clear the text
real_path="${raw_path#file://}"
real_path=$(printf '%b' "${real_path//%/\\x}")

# If it's an online radio or streaming service, we send the default.
if [[ "$real_path" == http* ]]; then
    echo "$DEFAULT_IMG"
    exit 0
fi

# 3. THE CACHE TRICK
HASH=$(echo -n "$real_path" | md5sum | awk '{print $1}')
COVER_PATH="$CACHE_DIR/${HASH}.jpg"

# If we had already removed it before, we return it immediately
if [[ -f "$COVER_PATH" ]]; then
    echo "$COVER_PATH"
    exit 0
fi

# 4. If it's new, we extract it with the ffmpeg patch (-update 1)
if [[ -f "$real_path" ]]; then
    ffmpeg -y -i "$real_path" -an -vframes 1 -update 1 -c:v mjpeg "$COVER_PATH" > /dev/null 2>&1

    if [[ $? -eq 0 && -f "$COVER_PATH" ]]; then
        echo "$COVER_PATH"
        exit 0
    fi
fi

# Fallback in case something goes wrong
echo "$DEFAULT_IMG"
