from fastapi import HTTPException, status

UserAlreadyExistsExeption = HTTPException(
    status_code=status.HTTP_409_CONFLICT, detail="User already exists"
)

IncorectUserNameExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorect user name or password"
)

NoTokenProvidedExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="No token provided "
)

TonetIsntFreshExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Tonet isn't fresh"
)
IncorrectTokenFormatExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorect token ormat"
)
NoUserWithThisIdExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User with provided id is not found",
)
JWTErrorExeption = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorect user name "
)
