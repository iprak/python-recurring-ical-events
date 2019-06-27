"""From https://tools.ietf.org/html/rfc5545#section-3.8.5.2

Property Name:  RDATE

   Purpose:  This property defines the list of DATE-TIME values for
      recurring events, to-dos, journal entries, or time zone
      definitions.

   Value Type:  The default value type for this property is DATE-TIME.
      The value type can be set to DATE or PERIOD.

   Property Parameters:  IANA, non-standard, value data type, and time
      zone identifier property parameters can be specified on this
      property.

   Conformance:  This property can be specified in recurring "VEVENT",
      "VTODO", and "VJOURNAL" calendar components as well as in the
      "STANDARD" and "DAYLIGHT" sub-components of the "VTIMEZONE"
      calendar component.

   Description:  This property can appear along with the "RRULE"
      property to define an aggregate set of repeating occurrences.
      When they both appear in a recurring component, the recurrence
      instances are defined by the union of occurrences defined by both
      the "RDATE" and "RRULE".

      The recurrence dates, if specified, are used in computing the
      recurrence set.  The recurrence set is the complete set of
      recurrence instances for a calendar component.  The recurrence set
      is generated by considering the initial "DTSTART" property along
      with the "RRULE", "RDATE", and "EXDATE" properties contained
      within the recurring component.  The "DTSTART" property defines
      the first instance in the recurrence set.  The "DTSTART" property
      value SHOULD match the pattern of the recurrence rule, if
      specified.  The recurrence set generated with a "DTSTART" property
      value that doesn't match the pattern of the rule is undefined.
      The final recurrence set is generated by gathering all of the
      start DATE-TIME values generated by any of the specified "RRULE"
      and "RDATE" properties, and then excluding any start DATE-TIME
      values specified by "EXDATE" properties.  This implies that start
      DATE-TIME values specified by "EXDATE" properties take precedence
      over those specified by inclusion properties (i.e., "RDATE" and
      "RRULE").  Where duplicate instances are generated by the "RRULE"
      and "RDATE" properties, only one recurrence is considered.
      Duplicate instances are ignored.
"""
import pytest

@pytest.mark.parametrize("day", "20130803 20130831 20131005 20131102 20131130 "
    "20140104 20140201 20140301 20140405 20140503 20140531 20140705".split())
def test_rdate_is_included(calendars, day):
    events = calendars.rdate_hackerpublicradio.at(day)
    assert len(events) == 1

def test_rdate_does_not_double_rrule_entry(todo):
    pass

def test_rdate_can_be_excluded_by_exdate(todo):
    pass

def test_rdate_and_rrule_can_be_excluded_by_exdate(todo):
    pass

def test_period_as_rdate(todo):
    """Test the PERIOD type.

    Value Type:  The default value type for this property is DATE-TIME.
       The value type can be set to DATE or PERIOD.
    """

def test_recurrence_length(todo):
    """
    When the combination of the "RRULE" and "RDATE" properties in a
    recurring component produces multiple instances having the same
    start DATE-TIME value, they should be collapsed to, and
    considered as, a single instance.  If the "RDATE" property is
    specified as a PERIOD value the duration of the recurrence
    instance will be the one specified by the "RDATE" property, and
    not the duration of the recurrence instance defined by the
    "DTSTART" property.
    """

def test_rdate_occurs_multiple_times(calendars):
    """An event can not only have an RDATE once but also many of them."""
    events = calendars.rdate_hackerpublicradio.all()
    assert len(events) == 12

def test_rdate_is_datetime(todo):
    pass

def test_rdate_is_date(todo):
    pass

def test_rdate_is_period(todo):
    pass

