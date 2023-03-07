from pathlib import Path

from runassociationtesting.module_loader import ModuleLoader
from test_loader import test_loader_ingester
from test_loader.test_loader_association_pack import TestLoaderProgramArgs, TestLoaderAssociationPack


class LoadModule(ModuleLoader):

    def __init__(self, output_prefix: str, input_args: str):

        super().__init__(output_prefix, input_args)

    def start_module(self) -> None:

        with Path('start_worked.txt').open('w') as worked_file:
            worked_file.write('module start worked')

        # Retrieve outputs – all tools _should_ append to the outputs object so they can be retrieved here.
        self.set_outputs(['start_worked.txt'])

    def _load_module_options(self) -> None:

        self._parser.add_argument('--run_marker_tests',
                                  help="Run per-marker tests for requested tool(s) [true]? Setting to false could "
                                       "DRASTICALLY reduce run-time (particularly if --tool saige). Only changes "
                                       "output for burden tests where tool = saige, regenie, or bolt.",
                                  dest='run_marker_tests', action='store_true')

    def _parse_options(self) -> TestLoaderProgramArgs:
        return TestLoaderProgramArgs(**vars(self._parser.parse_args(self._split_options(self._input_args))))

    def _ingest_data(self, parsed_options: TestLoaderProgramArgs) -> TestLoaderAssociationPack:
        ingested_data = test_loader_ingester.IngestData(parsed_options)
        return ingested_data.get_association_pack()
