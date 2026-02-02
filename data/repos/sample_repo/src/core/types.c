#include "core/types.h"

static const char *default_user_name = "guest";

UserRecord default_user(void) {
    UserRecord user;
    user.id = 0;
    user.name = default_user_name;
    return user;
}
