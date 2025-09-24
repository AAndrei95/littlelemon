# littlelemon

Paths:
GET /restaurant/home - Get Home page
GET /restaurant/menu - Get all menu items
POST /restaurant/menu - Create menu item
GET /restaurant/menu/<int> - Get single menu item
PUT /restaurant/menu/<int> - Update menu item
DELETE /restaurant/menu/<int> - Delete menu item
GET /restaurant/booking/ - Router
GET /restaurant/booking/tables - Get bookings
POST /restaurant/booking/tables - Create booking

-Registration using djoser-
Authentication:
POST /auth/token/login/ – Obtain authentication token
POST /auth/token/logout/ – Delete authentication token

Users:
POST /auth/users/ – Create a new user (register)
GET /auth/users/ – List users (if allowed)
GET /auth/users/me/ – Get current authenticated user
GET /auth/users/{id}/ – Retrieve a specific user
PUT /auth/users/me/ – Update current user
PATCH /auth/users/me/ – Partially update current user
DELETE /auth/users/me/ – Delete current user

Username:
POST /auth/users/set_username/ – Change username
POST /auth/users/reset_username/ – Request username reset
POST /auth/users/reset_username_confirm/ – Confirm username reset

Password:
POST /auth/users/set_password/ – Change password
POST /auth/users/reset_password/ – Request password reset email
POST /auth/users/reset_password_confirm/ – Confirm password reset