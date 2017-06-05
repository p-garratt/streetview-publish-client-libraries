<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/streetview/publish/v1/rpcmessages.proto

namespace Google\Streetview\Publish\V1;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * <pre>
 * Request to delete multiple photos.
 * </pre>
 *
 * Protobuf type <code>google.streetview.publish.v1.BatchDeletePhotosRequest</code>
 */
class BatchDeletePhotosRequest extends \Google\Protobuf\Internal\Message
{
    /**
     * <pre>
     * Required. List of delete photo requests.
     * </pre>
     *
     * <code>repeated string photo_ids = 1;</code>
     */
    private $photo_ids;

    public function __construct() {
        \GPBMetadata\Google\Streetview\Publish\V1\Rpcmessages::initOnce();
        parent::__construct();
    }

    /**
     * <pre>
     * Required. List of delete photo requests.
     * </pre>
     *
     * <code>repeated string photo_ids = 1;</code>
     */
    public function getPhotoIds()
    {
        return $this->photo_ids;
    }

    /**
     * <pre>
     * Required. List of delete photo requests.
     * </pre>
     *
     * <code>repeated string photo_ids = 1;</code>
     */
    public function setPhotoIds(&$var)
    {
        $arr = GPBUtil::checkRepeatedField($var, \Google\Protobuf\Internal\GPBType::STRING);
        $this->photo_ids = $arr;
    }

}

