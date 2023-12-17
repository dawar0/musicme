# Song Model

The `Song` model represents a musical composition and its associated information.

### Attributes:

- **id:** Integer, Primary Key
- **name:** String(80), Not Null
- **description:** String(120), Not Null
- **tags:** Many-to-Many Relationship with `Tag` through `SongTag`
- **image:** String(120), Not Null
- **song:** String(120), Not Null
- **artistId:** Integer, Foreign Key referencing `User.id`
- **artist:** Relationship with `User` model, representing the artist of the song

### Methods:

- **__repr__():** Provides a string representation of the `Song` object.

---

# Tag Model

The `Tag` model represents a tag associated with songs.

### Attributes:

- **id:** Integer, Primary Key
- **name:** String(80), Not Null
- **song:** Many-to-Many Relationship with `Song` through `SongTag`

### Methods:

- **__repr__():** Provides a string representation of the `Tag` object.

---

# User Model

The `User` model represents a user with attributes such as name, email, and songs created.

### Attributes:

- **id:** Integer, Primary Key
- **name:** String(80), Not Null, Unique
- **email:** String(120), Not Null, Unique
- **username:** String(120), Not Null, Unique
- **password:** String(120), Not Null, Unique
- **isAdmin:** Boolean, Nullable, Default: False
- **image:** String(120), Nullable
- **songs:** One-to-Many Relationship with `Song` model, representing songs created by the user

### Methods:

- **__repr__():** Provides a string representation of the `User` object.

---

# SongTag Model

The `SongTag` model represents a relationship between songs and tags.

### Attributes:

- **id:** Integer, Primary Key
- **show_id:** Integer, Foreign Key referencing `Song.id`, Not Null
- **tag_id:** Integer, Foreign Key referencing `Tag.id`, Not Null

### Methods:

- **__repr__():** Provides a string representation of the `SongTag` object.

