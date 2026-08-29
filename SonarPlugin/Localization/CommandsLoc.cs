using AG.EnumLocalization.Attributes;

namespace SonarPlugin.Localization
{
    [EnumLocStrings("Commands")]
    public enum CommandsLoc
    {
        [EnumLoc(Fallback = "Open/close Sonar's main window")]
        ToggleMainWindow,

        [EnumLoc(Fallback = "Open/close Sonar's configuration")]
        ToggleConfigWindow,

        [EnumLoc(Fallback = "Open/close Sonar's tracker")]
        ToggleTrackerWindow,

        [EnumLoc(Fallback = "Open/close Sonar errors window")]
        ToggleErrorWindow,

        [EnumLoc(Fallback = "Contact Sonar Support")]
        ContactSupport,

        [EnumLoc(Fallback = "Turn Global Contribute on")]
        TurnGlobalContributeOn,

        [EnumLoc(Fallback = "Turn Global Contribute off")]
        TurnGlobalContributeOff,

        [EnumLoc(Fallback = "Toggle Global Contribute on/off")]
        ToggleGlobalContribute,
    }
}
