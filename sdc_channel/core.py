import json
import os
from typing import Optional, List, Dict

from sdc_client import IStreamSets, IStreamSetsProvider, IPipeline, IPipelineProvider, ILogger


class Pipeline(IPipeline):
    def __init__(self, id_: str, config: dict):
        self.id = id_
        self.config = config
        self.streamsets = None

    def get_id(self) -> str:
        return self.id

    def get_config(self) -> dict:
        return self.config['pipelineConfig']

    def get_offset(self) -> Optional[str]:
        pass

    def get_streamsets(self) -> Optional[IStreamSets]:
        return self.streamsets

    def set_streamsets(self, streamsets: IStreamSets):
        self.streamsets = streamsets

    def delete_streamsets(self):
        self.streamsets = None


class StreamSets(IStreamSets):
    def get_id(self) -> int:
        return 1

    def get_url(self) -> str:
        if os.environ.get('ANTON'):
            return 'http://localhost:18630'
        return 'http://dc:18630'

    def get_username(self) -> str:
        return 'admin'

    def get_password(self) -> str:
        return 'admin'


class StreamsetsProvider(IStreamSetsProvider):
    def get(self, id_: int) -> IStreamSets:
        return StreamSets()

    def get_all(self) -> List[IStreamSets]:
        return [StreamSets()]


class PipelineProvider(IPipelineProvider):
    def get_pipelines(self) -> List[IPipeline]:
        return []

    def save(self, pipeline: IPipeline):
        pass

    def count_by_streamsets(self) -> Dict[int, int]:
        """ Returns { streamsets_id: number_of_pipelines } """
        return {
            1: 0
        }


class Logger(ILogger):
    def info(self, message: str):
        pass

    def error(self, message: str):
        pass

    def warning(self, message: str):
        pass


def get_base_config() -> dict:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'base_pipeline.json')) as f:
        return json.load(f)
