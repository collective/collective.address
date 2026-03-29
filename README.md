# collective.address

This package provides some [Dexterity
behavior](https://6.docs.plone.org/backend/behaviors.html) to be used in
[Dexterity based
types](https://6.docs.plone.org/backend/content-types/index.html) for:

`IAddress` behavior, some fields to describe the `Address` data.

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/iaddress_behavior.png"
width="732" height="79" alt="The IAddress Behavior" />
<figcaption>The <code>IAddress</code> Behavior.</figcaption>
</figure>

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/address_schema.png"
width="737" height="341"
alt="Using the IAddress Behavior into a custom content type." />
<figcaption aria-hidden="true">Using the <code>IAddress</code> Behavior
into a custom content type.</figcaption>
</figure>

---

`IContact` behavior, some fields to describe the `Contact` data.

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/icontact_behavior.png"
width="788" height="75" alt="The IContact Behavior" />
<figcaption>The <code>IContact</code> Behavior.</figcaption>
</figure>

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/contact_schema.png"
width="800" height="196"
alt="Using the IContact Behavior into a custom content type" />
<figcaption>Using the <code>IContact</code> Behavior into a custom
content type.</figcaption>
</figure>

---

`IPerson` behavior, some fields to describe the `Person` data.

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/iperson_behavior.png"
width="745" height="75" alt="The IPerson Behavior" />
<figcaption>The <code>IPerson</code> Behavior.</figcaption>
</figure>

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/person_schema.png"
width="778" height="81"
alt="Using the IPerson Behavior into a custom content type" />
<figcaption>Using the <code>IPerson</code> Behavior into a custom
content type.</figcaption>
</figure>

---

`ISocial` behavior, some fields to describe the `Person` data.

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/isocial_behavior.png"
width="778" height="81" alt="The ISocial Behavior" />
<figcaption>The <code>ISocial</code> Behavior.</figcaption>
</figure>

<figure class="align-center">
<img
src="https://raw.githubusercontent.com/collective/collective.address/refs/heads/master/docs/images/social_media_schema.png"
width="467" height="492"
alt="Using the ISocial Behavior into a custom content type." />
<figcaption aria-hidden="true">Using the <code>ISocial</code> Behavior
into a custom content type.</figcaption>
</figure>

---

# Examples

This add-on can be seen in action at the following add-ons:

- <https://github.com/collective/collective.venue>
- <https://github.com/g24at/g24.elements>
- <https://github.com/b4oshany/rohberg.bluechurch>
- <https://github.com/RedTurtle/iosanita.contenttypes>
- <https://github.com/RedTurtle/design.plone.ctgeneric>
- <https://github.com/RedTurtle/design.plone.contenttypes>

# Translations

This product has been translated into

- Deutsch
- Francese
- Italian
- Spanish

# Installation

If you installed Plone with
[Cookieplone](https://github.com/plone/cookieplone), you can install
`collective.address` add-on from a source control system such as GitHub.

Add a line with `collective.address` in the `backend/requirements.txt`
file.

    collective.address

Next add the add-on to `zcml_package_includes` in the file
`backend/instance.yaml` so that its configuration will load.

    default_context:
        zcml_package_includes: project_title, collective.address

Finally, add the package\'s source to the `mx.ini` file.

    [collective.address]
    url = https://github.com/collective/collective.address.git
    pushurl = git@github.com:collective/collective.address.git
    branch = master

To actually download and install the new add-on, run the following
command.

    make backend-build

Now restart the backend.

---

If you installed Plone with
[buildout](https://6.docs.plone.org/admin-guide/add-ons.html#buildout),
you can install `collective.address` add-on by adding it to your
`buildout` eggs list like so:

    [buildout]

    ...

    eggs =
        collective.address

and then running `bin/buildout`

Now restart the instance.

# Tips

The following are some tips on how to use this add-on.

## How to provide a default value for the country field

If you want to provide a default value for the `IAddress` country field,
you can provide an `ComputedWidgetAttribute` adapter like so:

    from zope.component import provideAdapter
    from z3c.form.widget import ComputedWidgetAttribute
    from collective.address.behaviors import IAddress

    DEFAULT_COUNTRY = "040"  # Austria
    provideAdapter(ComputedWidgetAttribute(
        lambda data: DEFAULT_COUNTRY,
        field=IAddress['country']), name='default')

The country code must be the numeric ISO 3166-1 code as a string. You
can find the list of codes here:
<https://en.wikipedia.org/wiki/ISO_3166-1_numeric>

If you want to play with the country codes in a Python shell, you can
use the `pycountry` package like so:

    >>> import pycountry
    >>> austria = pycountry.countries.get(numeric='040')
    >>> austria
    Country(alpha_2='AT', alpha_3='AUT', flag='🇦🇹', name='Austria', numeric='040', official_name='Republic of Austria')
    >>> spain = pycountry.countries.get(alpha_2='ES')
    >>> spain
    Country(alpha_2='ES', alpha_3='ESP', flag='🇪🇸', name='Spain', numeric='724', official_name='Kingdom of Spain')

You can install `pycountry` via pip:

    pip3 install pycountry

For more information, see the
[pycountry](https://pypi.org/project/pycountry/) documentation.

# Compatibility

- Tested with Python 3.12 and Plone 6.1.2.

# License

The project is licensed under the GPLv2.

# Contribute

- Issue Tracker:
  <https://github.com/collective/collective.address/issues>
- Source Code: <https://github.com/collective/collective.address>

# Author

- [Johannes Raggam](mailto:thetetet@gmail.com)
