from runassociationtesting.ingest_data import IngestData
from test_upload.test_upload_association_pack import TestUploadProgramArgs, TestUploadAssociationPack


class TestUploadIngestData(IngestData):

    def __init__(self, parsed_options: TestUploadProgramArgs):
        super().__init__(parsed_options)

        # Put additional covariate processing specific to this module here
        self.set_association_pack(TestUploadAssociationPack(self.get_association_pack()))
