#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from aospdtgen.proprietary_files.section import Section, register_section

class GatekeeperSection(Section):
	name = "Gatekeeper"
	interfaces = [
		"android.hardware.gatekeeper",
		"vendor.qti.hardware.secureprocessor",
		"vendor.qti.spu",
		"vendor.trustonic.tee",
	]
	hardware_modules = [
		"gatekeeper",
	]
	properties_prefixes = {
		"vendor.gatekeeper.": False,
	}

register_section(GatekeeperSection)
