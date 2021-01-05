from sqlalchemy import Column, String
from sdc_channel.core import Pipeline
from sdc_channel.db import Entity, session


class StreamsetsPipeline(Entity):
    __tablename__ = 'streamsets_pipelines'

    pipeline_id = Column(String, primary_key=True)
    streamsets_id = Column(String)

    def __init__(self, pipeline_id: str, streamsets_id: int):
        self.pipeline_id = pipeline_id
        self.streamsets_id = streamsets_id


def save(sp: StreamsetsPipeline):
    session().add(sp)
    session().commit()


def exists(pipeline: Pipeline) -> bool:
    return bool(session().query(
        session().query(StreamsetsPipeline).filter(StreamsetsPipeline.pipeline_id == pipeline.id).exists()
    ).scalar())


def get_by_pipeline(pipeline: Pipeline) -> StreamsetsPipeline:
    sp = session().query(Pipeline).filter(StreamsetsPipeline.pipeline_id == pipeline.id).first()
    if not sp:
        raise StreamsetsPipelineNotExistsException(f"Pipeline {pipeline.id} doesn't exist")
    return sp


class StreamsetsPipelineNotExistsException(Exception):
    pass
