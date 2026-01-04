### What
Added API to deactivate user using PATCH method.

### Why
Needed for admin to soft-disable users without deleting.

### How
- Used Django User model
- Added logging for success & failure
- Handled edge cases

### Testing
- Tested via Postman
