# Copyright (c) 2021-2024 Paulo Meira
from .common import Base
from typing import AnyStr, Optional, List

class IZIP(Base):
    __slots__ = []

    _columns = []

    def Open(self, FileName: AnyStr):
        '''
        Opens and prepares a ZIP file to be used by the DSS text parser.
        Currently, the ZIP format support is limited by what is provided in the Free Pascal distribution.
        Besides that, the full filenames inside the ZIP must be shorter than 256 characters.
        The limitations should be removed in a future revision.
        
        (API Extension)
        '''
        if not isinstance(FileName, bytes):
            FileName = FileName.encode(self._api_util.codec)

        self._check_for_error(self._lib.ZIP_Open(FileName))

    def Close(self):
        '''
        Closes the current open ZIP file
        
        (API Extension)
        '''
        self._check_for_error(self._lib.ZIP_Close())

    def Redirect(self, FileInZip: AnyStr):
        '''
        Runs a "Redirect" command inside the current (open) ZIP file.
        In the current implementation, all files required by the script must
        be present inside the ZIP, using relative paths. The only exceptions are
        memory-mapped files.

        (API Extension)
        '''
        if not isinstance(FileInZip, bytes):
            FileInZip = FileInZip.encode(self._api_util.codec)

        self._check_for_error(self._lib.ZIP_Redirect(FileInZip))

    def Extract(self, FileName: AnyStr) -> bytes:
        '''
        Extracts the contents of the file "FileName" from the current (open) ZIP file.
        Returns a byte-string.

        (API Extension)
        '''
        api_util = self._api_util
        if not isinstance(FileName, bytes):
            FileName = FileName.encode(api_util.codec)

        self._check_for_error(self._lib.ZIP_Extract_GR(FileName))
        ptr, cnt = api_util.gr_int8_pointers
        return bytes(api_util.ffi.buffer(ptr[0], cnt[0]))

    def List(self, regexp: Optional[AnyStr]=None) -> List[str]:
        '''
        List of strings consisting of all names match the regular expression provided in regexp.
        If no expression is provided, all names in the current open ZIP are returned.
        
        See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on 
        the expression syntax and options.

        (API Extension)
        '''
        if regexp is None or not regexp:
            regexp = self._api_util.ffi.NULL
        else:
            if not isinstance(regexp, bytes):
                regexp = regexp.encode(self._api_util.codec)
        
        return self._check_for_error(self._get_string_array(self._lib.ZIP_List, regexp))

    def Contains(self, Name: AnyStr) -> bool:
        '''
        Check if the given path name is present in the current ZIP file.
        
        (API Extension)
        '''
        if not isinstance(Name, bytes):
            Name = Name.encode(self._api_util.codec)

        return self._check_for_error(self._lib.ZIP_Contains(Name)) != 0

    def __getitem__(self, FileName) -> bytes:
        return self.Extract(FileName)

    def __contains__(self, Name) -> bool:
        return self.Contains(Name)

