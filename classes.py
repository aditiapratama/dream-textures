from .operators.install_dependencies import InstallDependencies
from .operators.open_latest_version import OpenLatestVersion
from .operators.dream_texture import DreamTexture, ReleaseGenerator, HeadlessDreamTexture
from .operators.view_history import SCENE_UL_HistoryList, RecallHistoryEntry, ClearHistory, RemoveHistorySelection, ExportHistorySelection, ImportPromptFile
from .operators.inpaint_area_brush import InpaintAreaStroke
from .operators.upscale import Upscale
from .property_groups.dream_prompt import DreamPrompt
from .ui.panels import dream_texture, history, upscaling, render_properties
from .preferences import OpenGitDownloads, OpenHuggingFace, OpenWeightsDirectory, OpenRustInstaller, ValidateInstallation, StableDiffusionPreferences

CLASSES = (
    HeadlessDreamTexture,
    *render_properties.render_properties_panels(),
    
    DreamTexture,
    ReleaseGenerator,
    OpenLatestVersion,
    SCENE_UL_HistoryList,
    RecallHistoryEntry,
    ClearHistory,
    RemoveHistorySelection,
    ExportHistorySelection,
    ImportPromptFile,
    InpaintAreaStroke,
    Upscale,
    
    # The order these are registered in matters
    *dream_texture.dream_texture_panels(),
    *upscaling.upscaling_panels(),
    *history.history_panels(),

    upscaling.OpenRealESRGANDownload,
    upscaling.OpenRealESRGANWeightsDirectory
)

PREFERENCE_CLASSES = (
                      DreamPrompt,
                      OpenGitDownloads,
                      InstallDependencies,
                      OpenHuggingFace,
                      OpenWeightsDirectory,
                      OpenRustInstaller,
                      ValidateInstallation,
                      StableDiffusionPreferences)