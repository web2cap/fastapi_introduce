from fastapi import HTTPException, status


class AppDefaultHTTPExeption(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


### Users and Auth
class UserAlreadyExistsExeption(AppDefaultHTTPExeption):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class IncorectUserNameExeption(AppDefaultHTTPExeption):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorect user name or password"


class NoTokenProvidedExeption(AppDefaultHTTPExeption):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "No token provided "


class TokenIsntFreshExeption(AppDefaultHTTPExeption):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Tonet isn't fresh"


class IncorrectTokenFormatExeption(AppDefaultHTTPExeption):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorect token ormat"


class NoUserWithThisIdExeption(AppDefaultHTTPExeption):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User with provided id is not found"


class JWTErrorExeption(AppDefaultHTTPExeption):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Incorect user name "


### boookings
class NoFreeRoomsOnThisDates(AppDefaultHTTPExeption):
    status_code = status.HTTP_409_CONFLICT
    detail = "There are no such rooms available for this dates"


# GENERAL
class NoEntryFoundException(AppDefaultHTTPExeption):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "No entry with provided id found"
