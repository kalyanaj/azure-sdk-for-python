# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .directory_object import DirectoryObject


class User(DirectoryObject):
    """Active Directory user information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar object_id: The object ID.
    :vartype object_id: str
    :ivar deletion_timestamp: The time at which the directory object was
     deleted.
    :vartype deletion_timestamp: datetime
    :param object_type: Constant filled by server.
    :type object_type: str
    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param immutable_id: This must be specified if you are using a federated
     domain for the user's userPrincipalName (UPN) property when creating a new
     user account. It is used to associate an on-premises Active Directory user
     account with their Azure AD user object.
    :type immutable_id: str
    :param usage_location: A two letter country code (ISO standard 3166).
     Required for users that will be assigned licenses due to legal requirement
     to check for availability of services in countries. Examples include:
     "US", "JP", and "GB".
    :type usage_location: str
    :param given_name: The given name for the user.
    :type given_name: str
    :param surname: The user's surname (family name or last name).
    :type surname: str
    :param user_type: A string value that can be used to classify user types
     in your directory, such as 'Member' and 'Guest'. Possible values include:
     'Member', 'Guest'
    :type user_type: str or ~azure.graphrbac.models.UserType
    :param account_enabled: Whether the account is enabled.
    :type account_enabled: bool
    :param display_name: The display name of the user.
    :type display_name: str
    :param user_principal_name: The principal name of the user.
    :type user_principal_name: str
    :param mail_nickname: The mail alias for the user.
    :type mail_nickname: str
    :param mail: The primary email address of the user.
    :type mail: str
    :param sign_in_names: The sign-in names of the user.
    :type sign_in_names: list[~azure.graphrbac.models.SignInName]
    """

    _validation = {
        'object_id': {'readonly': True},
        'deletion_timestamp': {'readonly': True},
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_id': {'key': 'objectId', 'type': 'str'},
        'deletion_timestamp': {'key': 'deletionTimestamp', 'type': 'iso-8601'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'immutable_id': {'key': 'immutableId', 'type': 'str'},
        'usage_location': {'key': 'usageLocation', 'type': 'str'},
        'given_name': {'key': 'givenName', 'type': 'str'},
        'surname': {'key': 'surname', 'type': 'str'},
        'user_type': {'key': 'userType', 'type': 'str'},
        'account_enabled': {'key': 'accountEnabled', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'mail_nickname': {'key': 'mailNickname', 'type': 'str'},
        'mail': {'key': 'mail', 'type': 'str'},
        'sign_in_names': {'key': 'signInNames', 'type': '[SignInName]'},
    }

    def __init__(self, additional_properties=None, immutable_id=None, usage_location=None, given_name=None, surname=None, user_type=None, account_enabled=None, display_name=None, user_principal_name=None, mail_nickname=None, mail=None, sign_in_names=None):
        super(User, self).__init__()
        self.additional_properties = additional_properties
        self.immutable_id = immutable_id
        self.usage_location = usage_location
        self.given_name = given_name
        self.surname = surname
        self.user_type = user_type
        self.account_enabled = account_enabled
        self.display_name = display_name
        self.user_principal_name = user_principal_name
        self.mail_nickname = mail_nickname
        self.mail = mail
        self.sign_in_names = sign_in_names
        self.object_type = 'User'
