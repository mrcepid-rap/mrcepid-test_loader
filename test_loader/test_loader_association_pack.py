from dataclasses import dataclass
from runassociationtesting.association_pack import AssociationPack, ProgramArgs


@dataclass
class TestLoaderProgramArgs(ProgramArgs):
    def _check_opts(self):
        pass


class TestLoaderAssociationPack(AssociationPack):

    def __init__(self, association_pack: AssociationPack):

        super().__init__(association_pack.is_binary, association_pack.sex, association_pack.threads,
                         association_pack.pheno_names, association_pack.found_quantitative_covariates,
                         association_pack.found_categorical_covariates, association_pack.cmd_executor)
