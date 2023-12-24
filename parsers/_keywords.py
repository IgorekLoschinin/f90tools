#!/usr/bin/venv python
# coding: utf-8


class Keywords(object):
	RENUMF90_keyword = {
		"DATAFILE",
		"SKIP_HEADER",
		"TRAITS",
		"FIELDS_PASSED TO OUTPUT",
		"WEIGHT(S)",
		"RESIDUAL_VARIANCE",
		"EFFECT",
		"NESTED",
		"RANDOM",
		"OPTIONAL",
		"FILE",
		"FILE_POS",
		"SNP_FILE",
		"PED_DEPTH",
		"GEN_INT",
		"REC_SEX",
		"UPG_TYPE",
		"INBREEDING",
		"(CO)VARIANCES",
		"(CO)VARIANCES_PE",
		"(CO)VARIANCES_PE",
		"(CO)VARIANCES_MPE",
		"COMBINE",
		"OPTION alpha_size",
		"OPTION max_string_readline",
		"OPTION max_field_readline",
	}

	# --------- BLUP ---------
	BLUPF90_keyword = {
		"OPTION conv_crit",
		"OPTION maxrounds",
		"OPTION solv_method",
		"OPTION r_factor",
		"OPTION sol",
		"OPTION blksize",
		"OPTION use_yams",
		"OPTION hetres_int",
		"OPTION fixed_var",
	}

	# ----------- Variance component estimation -----------
	REMLF90_keyword = {
		"OPTION conv_crit",
		"OPTION maxrounds",
		"OPTION sol",
		"OPTION",
		"OPTION constant_var",
		"OPTION missing",
		"OPTION use_yams",
		"OPTION SNP_file",
	}

	AIREMLF90_keyword = {
		"OPTION conv_crit",
		"OPTION maxrounds",
		"OPTION EM-REML",
		"OPTION sol",
		"OPTION tol",
		"OPTION fact_once",
		"OPTION constant_var",
		"OPTION missing",
		"OPTION use_yams",
		"OPTION approx_loglike",
		"OPTION hetres_pos",
		"OPTION hetres_pol",
		"OPTION SNP_file",
		"OPTION se_covar_function",
	}

	@property
	def unique_keywords(self) -> set[str]:
		return \
			self.__class__.RENUMF90_keyword | \
			self.__class__.BLUPF90_keyword | \
			self.__class__.REMLF90_keyword | \
			self.__class__.AIREMLF90_keyword

	@property
	def single_par(self) -> set[str]:
		return {
			'DATAFILE',
			'EFFECT',
			'FILE',
			'FILE_POS',
			'GEN_INT',
			'INBREEDING',
			'NESTED',
			'OPTIONAL',
			'PED_DEPTH',
			'RANDOM',
			'REC_SEX',
			'RESIDUAL_VARIANCE',
			'SNP_FILE',
			'TRAITS',
			'UPG_TYPE',
			'WEIGHT(S)',
			'(CO)VARIANCES',
			'(CO)VARIANCES_MPE',
			'(CO)VARIANCES_PE',
			'FIELDS_PASSED TO OUTPUT',
		}

	@property
	def complex_par(self) -> set[str]:
		return {
			'COMBINE',
			'OPTION'
		}
