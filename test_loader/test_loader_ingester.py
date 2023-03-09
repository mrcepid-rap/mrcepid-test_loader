from runassociationtesting.ingest_data import IngestData
from test_loader.test_loader_association_pack import TestLoaderProgramArgs, TestLoaderAssociationPack


class TestLoaderIngestData(IngestData):

    def __init__(self, parsed_options: TestLoaderProgramArgs):
        super().__init__(parsed_options)

        self.set_association_pack(TestLoaderAssociationPack(self.get_association_pack()))
