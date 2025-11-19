collective.address
==================

This package provides some `Dexterity behavior`_ to be used in `Dexterity based types`_ for:

- ``IAddress`` behavior, some fields to describe the ``Address`` data.

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/iaddress_behavior.png
    :align: center
    :height: 79px
    :width: 732px
    :alt: The IAddress Behavior

    The ``IAddress`` Behavior.

----

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/address_schema.png
    :align: center
    :height: 341px
    :width: 737px
    :alt: Using the IAddress Behavior into a custom content type.

    Using the ``IAddress`` Behavior into a custom content type.

- ``IContact`` behavior, some fields to describe the ``Contact`` data.

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/icontact_behavior.png
    :align: center
    :height: 75px
    :width: 788px
    :alt: The IContact Behavior

    The ``IContact`` Behavior.

----

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/contact_schema.png
    :align: center
    :height: 77px
    :width: 876px
    :alt: Using the IContact Behavior into a custom content type

    Using the ``IContact`` Behavior into a custom content type.

- ``IPerson`` behavior, some fields to describe the ``Person`` data.

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/iperson_behavior.png
    :align: center
    :height: 75px
    :width: 745px
    :alt: The IPerson Behavior

    The ``IPerson`` Behavior.

----

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/person_schema.png
    :align: center
    :height: 501px
    :width: 800px
    :alt: Using the IPerson Behavior into a custom content type

    Using the ``IPerson`` Behavior into a custom content type.

- ``ISocial`` behavior, some fields to describe the ``Person`` data.

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/isocial_behavior.png
    :align: center
    :height: 196px
    :width: 800px
    :alt: The ISocial Behavior

    The ``ISocial`` Behavior.

----

.. figure:: https://raw.githubusercontent.com/collective/collective.addressr/refs/heads/master/docs/images/social_media_schema.png
    :align: center
    :height: 492px
    :width: 467px
    :alt: Using the ISocial Behavior into a custom content type.

    Using the ``ISocial`` Behavior into a custom content type.


Examples
========

This add-on can be seen in action at the following add-ons:

- https://github.com/collective/collective.venue
- https://github.com/g24at/g24.elements
- https://github.com/b4oshany/rohberg.bluechurch
- https://github.com/RedTurtle/iosanita.contenttypes
- https://github.com/RedTurtle/design.plone.ctgeneric
- https://github.com/RedTurtle/design.plone.contenttypes


Translations
============

This product has been translated into

- Deutsch
- Francese
- Italian
- Spanish


Installation
============

If you installed Plone with `Cookieplone`_, you can install ``collective.address`` add-on 
from a source control system such as GitHub.

Add a line with ``collective.address`` in the ``backend/requirements.txt`` file.

::

    collective.address

Next add the add-on to ``zcml_package_includes`` in the file ``backend/instance.yaml`` so
that its configuration will load.

::

    default_context:
        zcml_package_includes: project_title, collective.address

Finally, add the package's source to the ``mx.ini`` file.

::

    [collective.address]
    url = https://github.com/collective/collective.address.git
    pushurl = git@github.com:collective/collective.address.git
    branch = master

To actually download and install the new add-on, run the following command.

::

    make backend-build

Now restart the backend.

----

If you installed Plone with `buildout`_, you can install ``collective.address`` add-on
by adding it to your ``buildout`` eggs list like so:

::

    [buildout]

    ...

    eggs =
        collective.address


and then running ``bin/buildout``

Now restart the instance.


Tips
====

The following are some tips on how to use this add-on.

How to provide a default value for the country field
----------------------------------------------------

If you want to provide a default value for the ``IAddress`` country field, you can
provide an ``ComputedWidgetAttribute`` adapter like so:

::

    from zope.component import provideAdapter
    from z3c.form.widget import ComputedWidgetAttribute
    from collective.address.behaviors import IAddress

    DEFAULT_COUNTRY = "040"  # Austria
    provideAdapter(ComputedWidgetAttribute(
        lambda data: DEFAULT_COUNTRY,
        field=IAddress['country']), name='default')

The country code must be the numeric ISO 3166-1 code as a string. You can find
the list of codes here: https://en.wikipedia.org/wiki/ISO_3166-1_numeric

If you want to play with the country codes in a Python shell, you can use the
``pycountry`` package like so:

::

    >>> import pycountry
    >>> austria = pycountry.countries.get(numeric='040')
    >>> austria
    Country(alpha_2='AT', alpha_3='AUT', flag='🇦🇹', name='Austria', numeric='040', official_name='Republic of Austria')
    >>> spain = pycountry.countries.get(alpha_2='ES')
    >>> spain
    Country(alpha_2='ES', alpha_3='ESP', flag='🇪🇸', name='Spain', numeric='724', official_name='Kingdom of Spain')

You can install ``pycountry`` via pip:

::

    pip3 install pycountry

For more information, see the `pycountry`_ documentation.


Compatibility
=============

- Tested with Python 3.12 and Plone 6.1.2.


License
=======

The project is licensed under the GPLv2.


Contribute
==========

- Issue Tracker: https://github.com/collective/collective.address/issues
- Source Code: https://github.com/collective/collective.address


Author
=======

- `Johannes Raggam <mailto:raggam-nl@adm.at>`_

.. _Dexterity behavior: https://6.docs.plone.org/backend/behaviors.html
.. _Dexterity based types: https://6.docs.plone.org/backend/content-types/index.html
.. _Cookieplone: https://github.com/plone/cookieplone
.. _pycountry: https://pypi.org/project/pycountry/
.. _buildout: https://6.docs.plone.org/admin-guide/add-ons.html#buildout
