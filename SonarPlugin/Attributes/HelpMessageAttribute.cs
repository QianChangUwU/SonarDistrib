using AG.EnumLocalization;
using SonarPlugin.Localization;
using System;

namespace SonarPlugin.Attributes
{
    [AttributeUsage(AttributeTargets.Method)]
    public sealed class HelpMessageAttribute : Attribute
    {
        public string HelpMessage { get; }

        public HelpMessageAttribute(string helpMessage)
        {
            HelpMessage = helpMessage;
        }

        public HelpMessageAttribute(CommandsLoc loc)
        {
            HelpMessage = loc.GetLocString();
        }
    }
}
